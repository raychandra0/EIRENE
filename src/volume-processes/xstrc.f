!pb  30.08.06: data structure for reaction data redefined
!pb  12.10.06: modcol revised
cdr  Jan. 2014:  minor bug in printout corrected
cdr  currently this routine is not called for RC processes, only for PH processes
cdr  Notation often just the other way round?

      SUBROUTINE EIRENE_XSTRC(ipls,nrc,idsc,irrc
     .                        rmass,ifrst,iscnd,     
     .                        eheavy,chrdf0,iscde,iestm,
     .                        kk,factkk)
cdr
cdr  to replace       ISWR==6, non-default RC part, as called from XSECTP.F
cdr  already done for ISWR==7 (photonic reaction part, "lines").
cdr  Prepare volume recombination processes: bulk (+ bulk)--> test (+ bulk)
cdr  e.g.   ISWR==6  (RC)                    H+    +  e   --> H    (+ rad.)
cdr  e.g.   ISWR==7  (PH)                    H(n=2)       --> Ly-alpha (+H(n=1))
cdr
c    ipls: incident bulk
c    nrc : index of reaction in list of all reactions for field particle IPLS
c    idsc: index of RC/PH reaction for species ipls
c    irrr: index of RC/PH reaction in NRRC/NRPH arrays
c
      USE EIRMOD_PRECISION
      USE EIRMOD_PARMMOD
      USE EIRMOD_COMUSR
      USE EIRMOD_COMPRT, ONLY: IUNOUT
      USE EIRMOD_COMXS
      USE EIRMOD_PHOTON

      IMPLICIT NONE
      integer, intent(in) :: ipls,nrc,idsc,irrc
      integer :: kk,ipl0,ipl1,ipl2,ityp0,ityp1,ityp2,
     .           j,orate,nserc3,nserc5,kread
      integer, external :: EIRENE_idez
      real(dp) :: factkk,aik
      EXTERNAL :: EIRENE_EXIT_OWN

c  fetch data for process nrc of ipls

      kk = IREACP(ipls,nrc)
c      if (kk /= idreac) call EIRENE_get_reaction(kk)

      FACTKK=FREACP(IPLS,NRC)
      IF (FACTKK.EQ.0.D0) FACTKK=1.
      aik=reacdat(kk)%phr%line%aik


      IPL0 =EIRENE_IDEZ(IBULKP(ipls,nrc),3,3)
      IPL1 =EIRENE_IDEZ(ISCD1P(ipls,nrc),3,3)
      IPL2 =EIRENE_IDEZ(ISCD2P(ipls,nrc),3,3)
      ITYP0=EIRENE_IDEZ(IBULKP(ipls,nrc),1,3)
      ITYP1=EIRENE_IDEZ(ISCD1P(ipls,nrc),1,3)
      ITYP2=EIRENE_IDEZ(ISCD2P(ipls,nrc),1,3)

      IF ((IPL0 < 1) .OR. (IPL0 > MAXSPC(ITYP0))) GOTO 993
      IF ((IPL1 < 1) .OR. (IPL1 > MAXSPC(ITYP1))) GOTO 994
      IF ((IPL2 < 1) .OR. (IPL2 > MAXSPC(ITYP2))) GOTO 994

      LGPRC(IPLS,IDSC)=IRRC

      facrrc(irrc,1) = factkk
      facrrc(irrc,2) = log(factkk)
      NREARC(irrc) = kk
      
      if (reacdat(kk)%lphr) then
! data type:  PH reaction, used here for an RC rate 
! controlled by   iftflg(kk,5),
!            also digit 6 of modclf(kk,...), and iswr(kk)=7   
! data format for this process kk: line_data
         
        aik=reacdat(kk)%phr%line%aik
cdr  this corresponds to iflflg(kk,5) >=  100: only a rate, not a rate coefficient     
        do j=1,nrad
          tabrc1(irrc,j)=aik*factkk
        enddo
cdr  we now use this type for a RC reaction        
        modcol(6,2,irrc)=1
        
      elseif (reacdat(kk)%loth) then
! data format: poly, adas, or crm (handled in subr. other_rate_coeff)
! data type: OT
! controlled by   iftflg(kk,5),
!            also digit 7 of modclf(kk,...), and iswr(kk)=8    
C
C  C  2.  EMISSIVITY (1/S) PER CELL
        ORATE=EIRENE_IDEZ(MODCLF(KK),7,7)       
C  
C  2.A)  = CONST.
C           TO BE WRITTEN
C  2.B) EMISSIVITY RATE OR RATE COEFFICIENT (T)
        IF (ORATE.EQ.1) THEN
          IF (NSTORDR >= NRAD) THEN

cdr  lexp should not be set from mod(iftflg),
cdr       that has completely different meaning !!!!!
            LEXP = .NOT. (MOD(IFTFLG(KK,5),100) == 10)


            DO J=1,NSBOX
              IF (LGVAC(J,IPLS)) CYCLE
              IF (LGVAC(J,NPLS+1).AND.IFTFLG(KK,5) < 100) CYCLE
              COU = EIRENE_OTHER_RATE_COEFF
     .                          (KK,J,TEINL(J),0._DP,LEXP,0)
              TABRC1(IRRC,J)=COU*FACTKK
              IF (IFTFLG(KK,2) < 100)
     .                TABRC1(IRRC,J)=TABRC1(IRRC,J)*DEIN(J)
            END DO
            NREARC(IRRC) = KK
          ELSE
C  DO NOT STORE DATA, BUT COMPUTE THEM WHEN NEEDED
            NREARC(IRRC) = KK
          END IF
          MODCOL(6,2,IRRC)=1
C       ELSEIF (ORATE.EQ.2) THEN
C  2.C) RATE(T,EBEAM): IRRELEVANT
        ELSEIF (ORATE.EQ.3) THEN
C  2.D) EMISSIVITY RATE or RATE COEFFICIENT(TE,NE)
          IF (NSTORDR >= NRAD) THEN
            DO J=1,NSBOX
              IF (LGVAC(J,IPLS)) CYCLE
              IF (LGVAC(J,NPLS+1).AND.IFTFLG(KK,5) < 100) CYCLE
              COU = EIRENE_OTHER_RATE_COEFF
     .                          (KK,J,TEINL(J),DEINL(J),.TRUE.,1)
              TABRC1(IRRC,J)=COU*FACTKK
              IF (IFTFLG(KK,5) < 100)
cdr  turn rate coefficient into a volumetric rate (1/s) to be multiplied
cdr  by emitter density and volume in samvol.f                    
     .          TABRC1(IRRC,J)=TABRC1(IRRC,J)*DEIN(J)
            END DO

            NREARC(IRRC) = KK
          ELSE
C  DO NOT STORE DATA, BUT COMPUTE THEM WHEN NEEDED
            NREARC(IRRC) = KK
          END IF
          MODCOL(6,2,IRRC)=1
        ENDIF  ! (MODCLF(KK),7,7) options (OT  type data) done   
      endif  ! all rates done: RT

C  4A  electron energy rates
      NSERC5=EIRENE_IDEZ(ISCDE,5,5)
C
C  4B  secondary particle energy rates
      NSERC3=EIRENE_IDEZ(ISCDE,3,5)
      
      if (nserc3 == 3) then
C  4.1C)  ENERGY LOSS RATE OF IMP. ION = EN.-WEIGHTED RATE
C       SAMPLE COLLIDING ION FROM DRIFTING MAXWELLIAN, WITH WEIGHTING/REJECTION
        KREAD=NINT(EHEAVY)
cdr  for the time being: KREAD must be a photonic rate, emission line data        
        NHVRRC(IRRC) = KREAD
        write (iunout,*) 'KREAD ',KREAD
      else
        write (iunout,*) 'shit'
        call eirene_exit_own(1)  
      endif             

      select case(ityp1)
      case(0)
         NPHPRC(IRRC)=IPL1
      case(1)
         NATPRC(IRRC)=IPL1
      case(2)
         NMLPRC(IRRC)=IPL1
      case(3)
         NIOPRC(IRRC)=IPL1
      case(4)
         NPLPRC(IRRC)=IPL1
      case default
         write(iunout,*) 'volume-processes: xstrc.f:'
         write(iunout,*) '   ityp1=',ityp1,' not allowed'
         call EIRENE_exit_own(1)
      end select
      select case(ityp2)
      case(0)
         NPHPRC_2(IRRC)=IPL2
      case(1)
         NATPRC_2(IRRC)=IPL2
      case(2)
         NMLPRC_2(IRRC)=IPL2
      case(3)
         NIOPRC_2(IRRC)=IPL2
      case(4)
         NPLPRC_2(IRRC)=IPL2
      case default
         write(iunout,*) 'volume-processes: xstrc.f:'
         write(iunout,*) '   ityp2=',ityp2,' not allowed'
         call EIRENE_exit_own(1)
      end select
      return

  993 CONTINUE
      WRITE (iunout,*) 'ERROR IN XSTRC: EXIT CALLED'
      WRITE (iunout,*)
     .  'SPECIES INDEX OF INCIDENT BULK PARTICLE OUT OF RANGE'
      WRITE (iunout,*) 'KK, ityp0, IPL0 ',
     .                  KK, ityp0, IPL0
      CALL EIRENE_EXIT_OWN(1)

  994 CONTINUE
      WRITE (iunout,*) 'ERROR IN XSTRC: EXIT CALLED'
      WRITE (iunout,*)
     .  'SPECIES INDEX OF SECONDARY PARTICLE OUT OF RANGE'
      WRITE (iunout,*) 'KK, ityp0, IPL0 ',
     .                  KK, ityp0, IPL0
      WRITE (iunout,*) 'ityp1, IPL1, itpy2, IPL2 ',
     .                  ityp1, IPL1, ityp2, IPL2
      CALL EIRENE_EXIT_OWN(1)

      END SUBROUTINE EIRENE_XSTRC

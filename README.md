# KISTI
get CPU, memory features in Nurion testbed using Linux perf stat

1. startcol.sh  : 모든 skl, knl 노드로 시작 명령을 보내는 스크립트.
2. collect/...  : perf stat을 이용해 skl, knl 노드별로 feature별 누적 count 값들을 5초마다 txt파일로 저장.
3. parse2csv.py : 위에서 노드별로 저장한 txt파일에서 필요한 정보만을 parsing하여 노드별/일별 csv파일로 저장.
4. dailycsv.sh  : 매일 새벽 1시 전날 하루에 쌓인 txt파일들에 대해 parse2csv.py를 실행 후 txt파일 삭제하는 코드.
5. module.py    : 1) 특정 darshan log file에서 jobid와 start time, end time을 추출하는 get_start_endtime()
                  2) start time과 같은 날짜의 sched log file에서 위에서 구한 jobid 가 사용한 node의 list를 알아내는 get_nodelit()
6. mean.py      : module의 두 함수를 이용해 특정 jobid가 특정 node들을 사용했을 때 그 time zone 주변의 hw/sw/cache 관련 feature들의 시간당 평균 발생횟수 및 표준편차 등을 확인 가능.





**1. 전체 코드 위치 Shared directory**

    1. /scratch/s5104a11/jwpyo
    
**2. 초기 경로지정**

    1. /scratch/s5104a11/jwpyo/collect/config.txt
    2. 작업위치(/scratch/s5104a11/jwpyo 를 대체), darshan log , schedule log path 총 3가지를 적어주면 됩니다.
    
**3. 순서**

    1. 데이터 수집 시작
    
        1. scratch/s5104a11/jwpyo/startcol.sh& 혹은 ./startcol.sh&  명령어로 백그라운드 실행을 시킵니다.
        2. scratch/s5104a11/jwpyo/D/ 에 노드별로 5초마다 누적 count들이 txt파일로 저장됩니다.
        
    2. 노드별 csv파일 생성
        1. 매일 새벽 한 시 전날의 데이터에 대해 노드별로 날짜별csv파일을 생성하게 됩니다. dailycsv.sh의 맨 아랫줄 주석(find ./ -name ‘$yesterday*’ -exec rm -f {} \;)을 해제해야 합니다. 
        2. (매일 1시에 돌아가는 코드는 0 1 * * * /scratch/s5104a11/jwpyo/dailycsv.sh   크론 명령어를 crontab에 저장해두었습니다. crontab -e로 수정가능합니다.)
        
    3. 피쳐별 평균구하기
        1. Module load python/3.7 명령 후 python3 mean.py 명령실행
        2. 원하는 darshanlog file 이름 입력-> 해당 시간대의 평균치 구할 수 있음

**4. 참고**

    1. 만약 vim으로 코드 수정 후 실행 시다음과 같은 에러가 난다면, (TabError: inconsistent use of tabs and spaces in indentation) 
    2. Vim 내부 코드를 다른데 붙여넣고 다시 복사해서 넣고 저장해주세요

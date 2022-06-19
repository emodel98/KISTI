# KISTI
get CPU, memory features in Nurion testbed using Linux perf stat

1. startcol.sh  : 모든 skl, knl 노드로 시작 명령을 보내는 스크립트.
2. collect/...  : perf stat을 이용해 skl, knl 노드별로 feature별 누적 count 값들을 5초마다 txt파일로 저장.
3. parse2csv.py : 위에서 노드별로 저장한 txt파일에서 필요한 정보만을 parsing하여 노드별/일별 csv파일로 저장한다.
4. dailycsv.sh  : 매일 새벽 1시 전날 하루에 쌓인 txt파일들에 대해 parse2csv.py를 실행 후 txt파일 삭제하는 코드( rm 부터 주석 해제해야 함. )
5. module.py    : 1) 특정 darshan log file에서 jobid와 start time, end time을 추출하는 get_start_endtime() 함수와
                  2) start time과 같은 날짜의 sched log file에서 위에서 구한 jobid 가 사용한 node의 list를 알아내는 get_nodelit() 함수 정의
6. mean.py      : module의 두 함수를 이용해 특정 jobid가 특정 node들을 사용했을 때 그 time zone 주변의 hw/sw/cache 관련 feature들의 시간당 평균 발생횟수 및 표준편차 등을 확인 가능.

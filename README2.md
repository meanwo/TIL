# git/git hub 정리 #



## 1. 사용자 정보 설정 ##

git config --global user.name "meanwo"
git config --global user.email "이메일 기입"



## 2. 깃허브 레포지토리 가져오기 ##

git clone 주소 : 원격 레포지토리를 로컬로 복사



## 3. 깃허브에 수정된 정보 반영하기

git add . (파일명을 타이핑, .은 모든 파일 추가)

git commit -m "Readme.md 추가"

git push 

---





## \* GIT 구조 및 관련 용어 ##

Work director: 내가 작업하고 있는 실제 디렉토리

​	git 이 관리하지 않는  파일 (git add를 추가하기 전 상태)



Staging Area: 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳



Repository: 커밋들이 저장되는 곳



Committed : commit 이 완료된 상태



-repository 에 반영된 상태



## \* GIT 관련 단축키 ##

Git init( 로컬 저장공간 생성)

 

Git status 입력 ( 현재 파일들의 상태를 출력)



Git log : git commit history 보기

Git log 명령어 종료는 'q' 입니다.

 

Git diff: 두 commit 간 차이 보기
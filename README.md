# 기말프로젝트

## 게임의 소개
1.제목: watch out!


2.게임의 목적: 광활한 우주에 표류된 주인공이 막무가내로 날아오는 운석을 피해서 안전한 목적지까지 도달하라!


3.게임 방법: 1인칭 시점의 플레이어가 날아오는 물체를 상하좌우키를 이용해서 피하고 공격버튼과 각종 아이템을 이용하여 물체를 피하는데 도움을 받는다.


### GameState (Scene)
1.titie_state


2.stater_state


3.game_state


4.image

#### GameState 세부사항
1.titie_state = 타이틀 화면


2.stater_state = 로고 화면


3.game_state = 게임 진행을 처리하는 부분


4.image = 이미지파일 저장소

.stater_state로 화면을시작해 로고를 띄우고 타이머를 지정해 일정 시간이 흐른후 title_state로 넘어가고 이 화면에서 게임시작 버튼과 간단한 게임조작키 설명을 안내해준다 title화면에서 spacebar 버튼을 누르면 게임진행화면인 game_state로 이동한다.

.처리해야할 키 목록:플레이어 조작키,아이템 사용키,공격 키,타이틀화면에서 메인화면으로 이동하는 키,게임종료 키

 # 개발 범위
  -1인칭 시점의 주인공캐릭터 시점 구현
  -날아오는 운석 움직임 구현
  -운석과 충돌시 충돌효과 구현
  -운석을 피하는데 도움을 주는 아이템 구현
  -사운드 구현
 
 ## 예상 게임 실행흐름
 ![image](https://user-images.githubusercontent.com/63137718/95847577-daf27180-0d87-11eb-98b4-9dc98d89735e.png)
 ![image](https://user-images.githubusercontent.com/63137718/95847715-02e1d500-0d88-11eb-9844-1230853a34c6.png)

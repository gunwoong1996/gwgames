# 기말프로젝트

# 게임의 소개
1.제목: watch out!


2.게임의 목적: 광활한 우주에 표류된 주인공이 막무가내로 날아오는 운석을 피해서 목적지까지 도달하라!


3.게임 방법:

 -플레이어가 날아오는 물체를 상하좌우키를 이용해서 피하고  각종 아이템을 이용하여 물체를 피하는데 도움을 받는다.
 
 -스테이지1은 운석을 피해서 우주선 부품을 다 모아야한다.
 
 -스테이지2는 우주선을타고 연료가 떨어지기전에 여러 장애물을 피해서 지구로 안전하게 도달해야한다

# 변경사항
 1인칭시점으로 정면에서 날아오는 객체를 표현하려고 했으나 1인칭 시점에서는 아이템을 포함한 여러가지 요소를 한눈에 보여주기가 힘들다고 생각하여
 교수님께 말씀드리고 정면이 아닌 사방에서 날아오는 객체를  표현하는것으로 변경함.
# 진행상황
![캡처](https://user-images.githubusercontent.com/63137718/99944071-a37ada00-2db5-11eb-9188-c76fcba9317b.PNG)


# git commit
![캡처](https://user-images.githubusercontent.com/63137718/99939338-2e0b0b80-2dad-11eb-83c1-a264e6c297b3.PNG)
![커밋주차별](https://user-images.githubusercontent.com/63137718/99939251-fe5c0380-2dac-11eb-8731-9a6bd683c4bd.PNG)


# GameState (Scene)
 main_state,generator,meteor,rockethead,rocketbody,rocketleft,rocketlight,shield,moveplayer,stage1bg,stage2bg,start_state,howtostage1
 

# GameState 세부사항
 ●1.main_state = 스테이지1 게임실행

 ●2.generator = 아이템 및 운석 움직임처리

 ●3.meteor = 운석

 ●4.rockethead = 로켓 머리
 
 ●5.rocketbody = 로켓 몸통
 
 ●6.rocketleft = 로켓 왼쪽날개
 
 ●7.rocketlight = 로켓 오른쪽날개
 
 ●8.shield = 쉴드 아이템
 
 ●9.moveplayer = 플레이어 움직임효과
 
 ●10.stage1bg = 스테이지1배경
 
 ●11.stage2bg = 스테이지2배경
 
 ●12.start_state = 시작화면
 
 ●13.howtostage1 = 스테이지1 설명

.처리해야할 키 목록:플레이어 조작키,타이틀화면에서 메인화면으로 이동하는 키,게임종료 키

 # 개발 범위
  -사방에서 날아오는 운석 구현
  
  -운석과 충돌시 충돌효과 구현
  
  -스테이지 클리어조건 구현
  
  -운석을 피하는데 도움을 주는 아이템 구현
  
  -사운드 구현
  
  -스테이지1,2구현
 
 # Class 구성정보
  class Move
  
  -플레이어의 움직임을 구현
  
  class Meteor
  
  -운석 구현
  
  class Shield
  
  -쉴드 아이템 구현
  
  class Rockethead
  
  -로켓 머리부분객체 구현
  
  class Rocketbody
  
  -로켓 몸통부분객체 구현
  
  class Rocketleft
  
  -로켓 왼쪽날개부분객체 구현
  
  class Rocketlight
  
  -로켓 오른쪽날개부분객체 구현
  
 
 ![캡처](https://user-images.githubusercontent.com/63137718/99942354-e5565100-2db2-11eb-9efa-0828a7ccf080.PNG)
 
 

 # 예상 게임 실행흐름
 ## 시작화면
 ![캡처](https://user-images.githubusercontent.com/63137718/99911715-a637e980-2d39-11eb-9a88-4a02049abc59.PNG)
 ## 스테이지설명
 ![캡처1](https://user-images.githubusercontent.com/63137718/99911717-a89a4380-2d39-11eb-8a4d-8330fb042293.PNG)
 ## 부품획득
 ![부품획득](https://user-images.githubusercontent.com/63137718/99942136-7ed13300-2db2-11eb-8d83-c5d353828028.gif)
 ## 쉴드아이템
 ![ezgif com-gif-maker](https://user-images.githubusercontent.com/63137718/99942362-e8514180-2db2-11eb-87b1-c9820a58e91c.gif)
 ## 1스테이지 클리어
 ![스테이지클리어](https://user-images.githubusercontent.com/63137718/99942156-8690d780-2db2-11eb-9b21-969799fb5c8a.gif)
 ## 게임오버
 ![게임오버](https://user-images.githubusercontent.com/63137718/99942164-885a9b00-2db2-11eb-9936-dcd803c23f30.gif)


 
 # 개발일정

![캡처](https://user-images.githubusercontent.com/63137718/97064983-222cfd80-15e5-11eb-8dd5-d49330c85b58.PNG)

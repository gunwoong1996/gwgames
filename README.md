# 기말프로젝트

## 게임의 소개
1.제목: watch out!


2.게임의 목적: 날아오는 물체를 피해 목적지까지 도달하여라.


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



# 윤년 판별기
4로 나누어 떨어지면 윤년
<br>
4와 100으로 나누어 떨어지면 평년
<br>
4와 100과 400으로 나누어 떨어지면 윤년
<br>
그 외 모든 연도는 평년
### 로직
조건문만 활용했다.

첫 조건문에서 4와 100으로 나누어 떨어지는 경우를 조건으로 걸었다.
<br>
첫 조건문 내부에서 400으로 나눠 떨어지냐를 중첩 `if`로 판단해서 참(0)일 때는 윤년
거짓(1)일 때는 평년
<br>
이후 두 번째 조건문에서 4로만 나누어 떨어지는 경우
<br>
`else`는 모두 평년으로 간주

참이 0이고 거짓이 1으로 설정한 거는 `== 0` 또는 `== 1` 이렇게 쓰기 싫어서 반전시킨 것

조건에 `not`을 걸어주면 참과 거짓이 반전된다
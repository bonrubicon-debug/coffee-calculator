import streamlit as st

st.set_page_config(page_title="나의 첫 Streamlit", page_icon="🌱")

st.title("🌱 나의 첫 Streamlit 앱")
st.write("이름을 입력하고 슬라이더를 움직여 보세요.")

# 입력한 내용은 name 변수에 담깁니다.
name = st.text_input("이름", value="새싹")
st.write(f"안녕하세요, {name}님!")

# 슬라이더를 움직이면 코드가 다시 실행되어 결과가 바뀝니다.
cups = st.slider("하루에 마시는 커피는 몇 잔인가요?", 0, 10, 2)
price = st.number_input("커피 한 잔 가격(원)", min_value=0, value=4500, step=500)
days = st.slider("며칠 동안 계산할까요?", 1, 365, 30)
st.metric(f"{days}일 동안의 커피 비용", f"{cups * price * days:,}원")

if st.button("응원받기"):
    st.success(f"{name}님, 첫 Streamlit 연습을 시작했어요!")

st.caption("첫 번째 미션: 하루 커피를 한 잔 줄이면 30일 비용이 얼마나 줄어들까요?")

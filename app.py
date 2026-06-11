import streamlit as st

st.set_page_config(
    page_title="AI 소비 습관 분석기",
    page_icon="💰"
)

st.title("💰 AI 소비 습관 분석 서비스")

st.write(
    "월별 소비 내역을 입력하면 AI가 소비 성향과 위험도를 분석합니다."
)

food = st.number_input("🍚 식비", min_value=0, step=10000)
cafe = st.number_input("☕ 카페", min_value=0, step=10000)
shopping = st.number_input("🛍 쇼핑", min_value=0, step=10000)
transport = st.number_input("🚌 교통", min_value=0, step=10000)
culture = st.number_input("🎬 문화생활", min_value=0, step=10000)

if st.button("🤖 AI 분석하기"):

    total = food + cafe + shopping + transport + culture

    if total == 0:
        st.warning("지출 금액을 입력해주세요.")
        st.stop()

    food_ratio = food / total * 100
    cafe_ratio = cafe / total * 100
    shopping_ratio = shopping / total * 100
    transport_ratio = transport / total * 100
    culture_ratio = culture / total * 100

    score = 100

    if shopping_ratio > 35:
        score -= 20

    if cafe_ratio > 20:
        score -= 10

    if culture_ratio > 25:
        score -= 5

    if food_ratio < 10:
        score -= 5

    score = max(score, 40)

    if score >= 85:
        risk = "🟢 낮음"
    elif score >= 70:
        risk = "🟡 보통"
    else:
        risk = "🔴 높음"

    if shopping_ratio >= max(food_ratio, cafe_ratio, transport_ratio, culture_ratio):
        style = "충동 소비형"
    elif culture_ratio >= max(food_ratio, cafe_ratio, shopping_ratio, transport_ratio):
        style = "경험 중시형"
    elif food_ratio >= 40:
        style = "생활 중심형"
    else:
        style = "균형 소비형"

    st.success("AI 분석 완료")

    st.subheader("📊 소비 성향 분석")

    st.write(f"소비 유형 : **{style}**")
    st.write(f"소비 건강 점수 : **{score}점**")
    st.write(f"소비 위험도 : **{risk}**")

    st.subheader("📈 지출 비중")

    st.write(f"식비 : {food_ratio:.1f}%")
    st.write(f"카페 : {cafe_ratio:.1f}%")
    st.write(f"쇼핑 : {shopping_ratio:.1f}%")
    st.write(f"교통 : {transport_ratio:.1f}%")
    st.write(f"문화생활 : {culture_ratio:.1f}%")

    st.subheader("🧠 AI 분석 의견")

    if food_ratio > 35:
        st.write(
            "식비 비중은 다소 높지만 생활 필수 지출의 특성을 고려할 때 정상 범위로 판단됩니다."
        )

    if shopping_ratio > 30:
        st.write(
            "쇼핑 비중이 높아 충동구매 가능성이 있습니다."
        )

    if cafe_ratio > 15:
        st.write(
            "카페 소비가 높은 편입니다. 주 1~2회만 줄여도 상당한 절약 효과를 기대할 수 있습니다."
        )

    if culture_ratio > 20:
        st.write(
            "문화생활 지출이 활발합니다. 삶의 만족도를 높이는 긍정적인 소비로 볼 수 있습니다."
        )

    st.subheader("💡 AI 절약 제안")

    yearly_save = int(cafe * 0.2 * 12)

    st.write(
        f"""
카페 소비를 20% 줄일 경우

예상 연간 절약 금액 :
약 {yearly_save:,}원

절약 금액을 투자나 저축에 활용하면 장기적인 자산 형성에 도움이 됩니다.
"""
    )

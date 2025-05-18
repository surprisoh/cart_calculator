import streamlit as st
import pandas as pd

# 상품 데이터
products = [{'id': 0,
  'name': '절단 대파 500g',
  'sellers': [{'name': '쿠팡', 'price': 1790}, {'name': '와이즐리', 'price': 2190}]},
 {'id': 1,
  'name': '유부초밥 320g',
  'sellers': [{'name': '쿠팡', 'price': 3980}, {'name': '와이즐리', 'price': 2990}]},
 {'id': 2,
  'name': '바나나 1kg',
  'sellers': [{'name': '쿠팡', 'price': 1980}, {'name': '와이즐리', 'price': 2990}]},
 {'id': 3,
  'name': '무항생제 계란 30구',
  'sellers': [{'name': '쿠팡', 'price': 10180},
   {'name': '와이즐리', 'price': 6490}]},
 {'id': 4,
  'name': '국내산 청양고추 150g',
  'sellers': [{'name': '쿠팡', 'price': 1400}, {'name': '와이즐리', 'price': 1190}]},
 {'id': 5,
  'name': '국내산 애호박 1개',
  'sellers': [{'name': '쿠팡', 'price': 990}, {'name': '와이즐리', 'price': 1190}]},
 {'id': 6,
  'name': '왕교자 1kg',
  'sellers': [{'name': '쿠팡', 'price': 9050}, {'name': '와이즐리', 'price': 7190}]},
 {'id': 7,
  'name': '국내산 25년 햇 양파 1.5kg',
  'sellers': [{'name': '쿠팡', 'price': 4490}, {'name': '와이즐리', 'price': 4490}]},
 {'id': 8,
  'name': '국내산 새송이버섯 3~4개입(400g/봉)',
  'sellers': [{'name': '쿠팡', 'price': 2690}, {'name': '와이즐리', 'price': 2290}]},
 {'id': 9,
  'name': '국내산 팽이버섯 150g 2입',
  'sellers': [{'name': '쿠팡', 'price': 1160}, {'name': '와이즐리', 'price': 890}]},
 {'id': 10,
  'name': '떡갈비 (100g * 6입)',
  'sellers': [{'name': '쿠팡', 'price': 20000},
   {'name': '와이즐리', 'price': 7490}]},
 {'id': 11,
  'name': '한우 대창 쭈꾸미 320g',
  'sellers': [{'name': '쿠팡', 'price': 13900},
   {'name': '와이즐리', 'price': 7490}]},
 {'id': 12,
  'name': '후랑크소시지 275g*2팩',
  'sellers': [{'name': '쿠팡', 'price': 8980}, {'name': '와이즐리', 'price': 3840}]},
 {'id': 13,
  'name': '국산 오븐구이 치킨 (1kg 내외)',
  'sellers': [{'name': '쿠팡', 'price': 8900}, {'name': '와이즐리', 'price': 5990}]},
 {'id': 14,
  'name': '송탄식 부대찌개 1kg',
  'sellers': [{'name': '쿠팡', 'price': 8240}, {'name': '와이즐리', 'price': 5790}]},
 {'id': 15,
  'name': '돼지고기 앞다리 500g',
  'sellers': [{'name': '쿠팡', 'price': 8580}, {'name': '와이즐리', 'price': 6490}]},
 {'id': 16,
  'name': '깐마늘 300g',
  'sellers': [{'name': '쿠팡', 'price': 4200}, {'name': '와이즐리', 'price': 3390}]}]
# 세션 상태 초기화
if "cart" not in st.session_state:
    st.session_state.cart = []

if "added_ids" not in st.session_state:
    st.session_state.added_ids = []

st.title("🛒 판매처별 장바구니 총합 계산기")

# 상품 검색
query = st.text_input("상품명을 검색해주세요.", "")
filtered_products = [p for p in products if query in p["name"]]

# 검색 결과 출력

st.subheader("🔍 검색 결과")
with st.container():
    st.markdown(
        "<div style='max-height: 30px; overflow-y: auto;'>",
        unsafe_allow_html=True
    )

    for p in filtered_products:
        # 모바일에 적합한 컬럼 비율 조정 (5:1:1 비율 → 더 여유 있게)
        col1, col2, col3 = st.columns([6, 2, 1])
        with col1:
            st.markdown(f"<div style='font-size: 16px; padding: 4px 0;'>{p['name']}</div>", unsafe_allow_html=True)
        with col2:
            if st.button("담기" if p['id'] not in st.session_state.added_ids else "제거", key=f"toggle_{p['id']}"):
                if p['id'] in st.session_state.added_ids:
                    st.session_state.cart = [item for item in st.session_state.cart if item["id"] != p["id"]]
                    st.session_state.added_ids.remove(p['id'])
                else:
                    st.session_state.cart.append(p)
                    st.session_state.added_ids.append(p['id'])
        with col3:
            if p['id'] in st.session_state.added_ids:
                st.markdown("<div style='font-size: 18px; padding: 4px 0;'>✅</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# 장바구니 출력
st.subheader("🧺 장바구니")
if st.session_state.cart:
    cart_list = []
    # print(st.session_state.cart)
    # print(p['sellers'])


    for p in st.session_state.cart:
        cart_data = {'상품명' : p['name'], 
                            '쿠팡 상품명' : [p['name'] + '_수정필요' for k in p['sellers'] if k['name'] == '쿠팡'][0],
                            '쿠팡 판매가' : [k['price'] for k in p['sellers'] if k['name'] == '쿠팡'][0],
                            '와이즐리 상품명' : [p['name'] + '_수정필요' for k in p['sellers'] if k['name'] == '와이즐리'][0],
                            '와이즐리 판매가' : [k['price'] for k in p['sellers'] if k['name'] == '와이즐리'][0]
                            }
        cart_list.append(cart_data)
        cart_df = pd.DataFrame(cart_list)
        # print(cart_df)
    st.table(cart_df)
    # st.write(f"- {p['name']}")
        

    # 판매처별 총합 계산
    seller_totals = {}
    for item in st.session_state.cart:
        for seller in item["sellers"]:
            name = seller["name"]
            price = seller["price"]
            if name not in seller_totals:
                seller_totals[name] = 0
            seller_totals[name] += price

    st.subheader("📦 판매처별 총합")
    df_summary = pd.DataFrame([
        {"판매처": k, "총합 (원)": v} for k, v in seller_totals.items()
    ])
    st.table(df_summary)
    lowest_price_seller = df_summary.iloc[df_summary['총합 (원)'].idxmin()]['판매처']
    st.write('{seller}에서 구매하는게 가장 저렴합니다!'.format(seller=lowest_price_seller))

else:
    st.write("장바구니가 비어 있습니다.")

# 장바구니 초기화
if st.button("🗑 장바구니 비우기"):
    st.session_state.cart = []
    st.session_state.added_ids = []
    st.experimental_rerun()  # 🔁 UI를 즉시 새로고침

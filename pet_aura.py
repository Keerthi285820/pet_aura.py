import streamlit as st

# Dummy cat data
cats = [
    {
        "id": 1,
        "name": "Persian Cat",
        "price": "₹15,000",
        "desc": "Long-haired, affectionate and quiet breed.",
        "img": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg"
    },
    {
        "id": 2,
        "name": "Siamese Cat",
        "price": "₹12,000",
        "desc": "Sleek, elegant, vocal and affectionate.",
        "img": "https://cdn2.thecatapi.com/images/ai6Jps4sx.jpg"
    },
    {
        "id": 3,
        "name": "Maine Coon",
        "price": "₹18,000",
        "desc": "Big, fluffy, and very gentle breed.",
        "img": "https://cdn2.thecatapi.com/images/OD3N9Zzdo.jpg"
    }
]

# Navigation
st.set_page_config(page_title="Petaura - Cat Pet Shop", layout="wide")
st.title("🐱 Petaura - Cat Pet Shop")

if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_cat" not in st.session_state:
    st.session_state.selected_cat = None
if "order_placed" not in st.session_state:
    st.session_state.order_placed = False

def go_to_page(page):
    st.session_state.page = page

def select_cat(cat):
    st.session_state.selected_cat = cat
    go_to_page("details")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.button("🏠 Home", on_click=lambda: go_to_page("home"))
st.sidebar.button("🐾 View All Cats", on_click=lambda: go_to_page("catalog"))

if st.session_state.page == "home":
    st.subheader("Welcome to Petaura 🐾")
    st.markdown("Your one-stop shop for adorable cat companions! Explore and adopt your furry friend today.")
    st.image("https://cdn2.thecatapi.com/images/8b8.jpg", width=600)

elif st.session_state.page == "catalog":
    st.subheader("🐱 Our Cat Collection")
    cols = st.columns(3)
    for idx, cat in enumerate(cats):
        with cols[idx % 3]:
            st.image(cat["img"], width=200)
            st.markdown(f"**{cat['name']}**")
            st.markdown(cat["price"])
            if st.button(f"View Details - {cat['id']}"):
                select_cat(cat)

elif st.session_state.page == "details":
    cat = st.session_state.selected_cat
    if cat:
        st.image(cat["img"], width=400)
        st.subheader(cat["name"])
        st.markdown(f"**Price:** {cat['price']}")
        st.markdown(cat["desc"])
        if st.button("🐾 Adopt Now"):
            go_to_page("order")
    else:
        st.warning("No cat selected. Go back to the catalog.")
        go_to_page("catalog")

elif st.session_state.page == "order":
    st.subheader("🐾 Place Your Order")
    with st.form("order_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        address = st.text_area("Delivery Address")
        cat_name = st.session_state.selected_cat["name"] if st.session_state.selected_cat else "Unknown"
        submitted = st.form_submit_button("Confirm Order")
        if submitted:
            st.session_state.order_placed = True
            st.session_state.customer = {
                "name": name,
                "email": email,
                "address": address,
                "cat": cat_name
            }
            go_to_page("confirmation")

elif st.session_state.page == "confirmation":
    if st.session_state.order_placed:
        customer = st.session_state.customer
        st.success("🎉 Order Placed Successfully!")
        st.markdown(f"**Thank you, {customer['name']}!**")
        st.markdown(f"You have adopted: **{customer['cat']}**")
        st.markdown(f"Confirmation sent to: **{customer['email']}**")
        st.markdown("📦 Your furry friend will be on their way soon!")
    else:
        st.warning("No order found.")
        go_to_page("home")

import streamlit as st

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown("""
    <div style='text-align:center;padding-top:50px'>
        <h1 style='color:green;'>
            🌴 Anumolu's Palm Oil Management System
        </h1>
        <h3>Harvest Tracking & Revenue Management</h3>
        <br>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1518495973542-4542c06a5843",
        use_container_width=True
    )

    if st.button("🚀 Enter Application"):
        st.session_state.started = True
        st.rerun()

    st.stop()

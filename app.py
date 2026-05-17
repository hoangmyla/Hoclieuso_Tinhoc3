
import streamlit as st
import random
import base64

# =====================================================
# CẤU HÌNH TRANG
# =====================================================
st.set_page_config(
    page_title="Học liệu số Tin học 3",
    page_icon="💻",
    layout="centered"
)

# =====================================================
# CSS GIAO DIỆN
# =====================================================
st.markdown("""
<style>

/* NỀN CHUNG */
.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
    background-attachment: fixed;
}

/* ẨN MENU */
#MainMenu {
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* KHUNG CHUNG */
.card{
    background: rgba(255,255,255,0.22);
    backdrop-filter: blur(12px);

    padding:25px;

    border-radius:25px;

    border:1px solid rgba(255,255,255,0.3);

    box-shadow:0 8px 32px rgba(31,38,135,0.2);

    margin-top:20px;
}

/* TIÊU ĐỀ */
.title-row{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;

    margin-top:10px;
    margin-bottom:10px;
}

.main-title{
    font-size:38px;
    font-weight:bold;
    color:white;
    text-shadow:2px 2px 5px rgba(0,0,0,0.2);
    text-align:center;
    width:100%;
}

/* PHỤ ĐỀ */
.sub-title{
    text-align:center;
    font-size:20px;
    color:white;
    margin-bottom:25px;
    width:100%;
}

/* NÚT */
.stButton button{

    width:100%;

    height:60px;

    border-radius:18px;

    border:none;

    font-size:19px;

    font-weight:bold;

    background:linear-gradient(90deg,#667eea,#764ba2);

    color:white;

    transition:0.3s;
}

.stButton button:hover{

    transform:scale(1.03);

    box-shadow:0 5px 15px rgba(0,0,0,0.2);
}

/* ĐIỂM */
.score-box{

    background:linear-gradient(90deg,#11998e,#38ef7d);

    padding:15px;

    border-radius:18px;

    text-align:center;

    color:white;

    font-size:24px;

    font-weight:bold;

    margin-top:10px;
}

/* DANH HIỆU */
.reward-box{

    background:linear-gradient(90deg,#f7971e,#ffd200);

    padding:20px;

    border-radius:20px;

    text-align:center;

    color:white;

    font-size:30px;

    font-weight:bold;

    margin-top:20px;
}

/* CÂU HỎI */
.question-box{

    background:white;

    padding:20px;

    border-radius:20px;

    box-shadow:0 5px 15px rgba(0,0,0,0.1);

    margin-top:15px;
}

/* FOOTER */
.footer{
    text-align:center;
    color:white;
    margin-top:30px;
    font-size:17px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# ÂM THANH
# =====================================================
def autoplay_audio(file_path):

    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay>
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

# =====================================================
# DỮ LIỆU CÂU HỎI
# =====================================================
topics = {

# =====================================================
# CHỦ ĐỀ A
# =====================================================
"A. Máy tính và em":[

{
"question":"Bộ phận nào giúp nhập chữ vào máy tính?",
"options":["Chuột","Loa","Bàn phím"],
"answer":"Bàn phím"
},

{
"question":"Máy tính xách tay còn gọi là?",
"options":["Máy in","Laptop","Loa"],
"answer":"Laptop"
},

{
"question":"Chuột máy tính dùng để?",
"options":["Nghe nhạc","Điều khiển","In giấy"],
"answer":"Điều khiển"
},

{
"question":"Ngồi máy tính đúng nên cách màn hình?",
"options":["2 m","50-80 cm","10 cm"],
"answer":"50-80 cm"
},

{
"question":"Thông tin em nghe được là dạng?",
"options":["Văn bản","Âm thanh","Hình ảnh"],
"answer":"Âm thanh"
},

{
"question":"Bộ não của máy tính là?",
"options":["Chuột","Thân máy","Loa"],
"answer":"Thân máy"
},

{
"question":"Hai phím có gai là?",
"options":["R và U","F và J","G và H"],
"answer":"F và J"
},

{
"question":"Ngồi máy tính lâu dễ bị?",
"options":["Sâu răng","Cận thị","Đau bụng"],
"answer":"Cận thị"
},

{
"question":"Màn hình dùng để?",
"options":["Phát âm thanh","Hiển thị hình ảnh","Gõ chữ"],
"answer":"Hiển thị hình ảnh"
},

{
"question":"Máy tính giúp em?",
"options":["Đá bóng","Học tập","Ngủ"],
"answer":"Học tập"
}

],

# =====================================================
# CHỦ ĐỀ B
# =====================================================
"B. Mạng máy tính và Internet":[

{
"question":"Internet giúp em?",
"options":["Giặt quần áo","Tìm thông tin","Nấu cơm"],
"answer":"Tìm thông tin"
},

{
"question":"Biểu tượng kính lúp dùng để?",
"options":["In","Tìm kiếm","Tắt máy"],
"answer":"Tìm kiếm"
},

{
"question":"Không nên làm gì trên mạng?",
"options":["Xem tin","Kết bạn người lạ","Học tập"],
"answer":"Kết bạn người lạ"
},

{
"question":"Khi gặp nội dung xấu em nên?",
"options":["Tiếp tục xem","Báo người lớn","Chia sẻ"],
"answer":"Báo người lớn"
},

{
"question":"Internet là?",
"options":["Loa","Máy in","Mạng máy tính"],
"answer":"Mạng máy tính"
},

{
"question":"Trang web giúp em?",
"options":["Đọc tin","Nấu ăn","Giặt đồ"],
"answer":"Đọc tin"
},

{
"question":"Khi dùng Internet cần?",
"options":["Cãi nhau","An toàn","Nói tục"],
"answer":"An toàn"
},

{
"question":"Thiết bị kết nối Internet không dây là?",
"options":["Chuột","WiFi","Loa"],
"answer":"WiFi"
},

{
"question":"Xem thông tin trên Internet cần?",
"options":["Chọn lọc","Tin hết","Chia sẻ hết"],
"answer":"Chọn lọc"
},

{
"question":"Internet hỗ trợ em?",
"options":["Ngủ","Học trực tuyến","Đá bóng"],
"answer":"Học trực tuyến"
}

],

# =====================================================
# CHỦ ĐỀ C
# =====================================================
"C. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin":[

{
"question":"Thư mục dùng để?",
"options":["Nghe nhạc","Lưu dữ liệu","Nấu cơm"],
"answer":"Lưu dữ liệu"
},

{
"question":"Cây thư mục giúp?",
"options":["Vẽ tranh","Sắp xếp dữ liệu","Nghe nhạc"],
"answer":"Sắp xếp dữ liệu"
},

{
"question":"Tên thư mục nên?",
"options":["Ngẫu nhiên","Dễ hiểu","Khó nhớ"],
"answer":"Dễ hiểu"
},

{
"question":"Muốn mở thư mục em?",
"options":["Tắt máy","Nháy đúp chuột","Rút điện"],
"answer":"Nháy đúp chuột"
},

{
"question":"Biểu tượng thư mục thường màu?",
"options":["Đen","Vàng","Đỏ"],
"answer":"Vàng"
},

{
"question":"Sắp xếp dữ liệu giúp?",
"options":["Khó tìm","Dễ tìm","Mất dữ liệu"],
"answer":"Dễ tìm"
},

{
"question":"Tệp dữ liệu còn gọi là?",
"options":["Slide","File","WiFi"],
"answer":"File"
},

{
"question":"Sơ đồ hình cây dùng để?",
"options":["Nghe nhạc","Phân loại","In giấy"],
"answer":"Phân loại"
},

{
"question":"Có nên lưu dữ liệu lộn xộn?",
"options":["Tùy thích","Không","Có"],
"answer":"Không"
},

{
"question":"Máy tính giúp lưu?",
"options":["Nước","Thông tin","Thức ăn"],
"answer":"Thông tin"
}

],

# =====================================================
# CHỦ ĐỀ D
# =====================================================
"D. Đạo đức, pháp luật và văn hoá trong môi trường số":[

{
"question":"Có nên cho người lạ biết mật khẩu?",
"options":["Không","Có","Tùy thích"],
"answer":"Không"
},

{
"question":"Thông tin cá nhân cần?",
"options":["Công khai","Cho hết","Bảo mật"],
"answer":"Bảo mật"
},

{
"question":"Khi dùng Internet cần?",
"options":["Nói to","Lịch sự","Cãi nhau"],
"answer":"Lịch sự"
},

{
"question":"Có nên bắt nạt trên mạng?",
"options":["Không","Có","Đôi khi"],
"answer":"Không"
},

{
"question":"Môi trường số cần?",
"options":["Nguy hiểm","An toàn","Lộn xộn"],
"answer":"An toàn"
},

{
"question":"Nên đặt mật khẩu như thế nào?",
"options":["123456","abc","Khó đoán"],
"answer":"Khó đoán"
},

{
"question":"Khi gặp người xấu trên mạng cần?",
"options":["Báo người lớn","Làm quen","Cho thông tin"],
"answer":"Báo người lớn"
},

{
"question":"Có nên đăng địa chỉ nhà lên mạng?",
"options":["Có","Đôi khi","Không"],
"answer":"Không"
},

{
"question":"Trên mạng cần cư xử?",
"options":["Gây gổ","Văn minh","Thô lỗ"],
"answer":"Văn minh"
},

{
"question":"Bảo vệ thông tin cá nhân là?",
"options":["Quan trọng","Không cần","Vô ích"],
"answer":"Quan trọng"
}

],

# =====================================================
# CHỦ ĐỀ E
# =====================================================
"E. Ứng dụng tin học":[

{
"question":"Slide dùng để?",
"options":["Trình chiếu","Ngủ","Nấu ăn"],
"answer":"Trình chiếu"
},

{
"question":"Mouse Skills giúp?",
"options":["Luyện hát","Luyện chuột","Luyện chạy"],
"answer":"Luyện chuột"
},

{
"question":"Slide có thể chứa?",
"options":["Nước","Chữ và hình","Bánh"],
"answer":"Chữ và hình"
},

{
"question":"Máy tính giúp quan sát?",
"options":["Núi thật","Mưa thật","Hạt đậu nảy mầm"],
"answer":"Hạt đậu nảy mầm"
},

{
"question":"Tin học giúp em?",
"options":["Học tốt hơn","Lười học","Ngủ nhiều"],
"answer":"Học tốt hơn"
},

{
"question":"Phần mềm trình chiếu giúp?",
"options":["Giặt đồ","Trình bày bài học","Nấu cơm"],
"answer":"Trình bày bài học"
},

{
"question":"Có thể thêm gì vào slide?",
"options":["Nước","Cơm","Hình ảnh"],
"answer":"Hình ảnh"
},

{
"question":"Chuột giúp em?",
"options":["Điều khiển","Nghe nhạc","In giấy"],
"answer":"Điều khiển"
},

{
"question":"Máy tính giúp em khám phá?",
"options":["Xe máy","Thế giới tự nhiên","Đồ chơi",],
"answer":"Thế giới tự nhiên"
},

{
"question":"Slide đẹp cần?",
"options":["Rõ ràng","Rối mắt","Quá nhiều chữ"],
"answer":"Rõ ràng"
}

],

# =====================================================
# CHỦ ĐỀ F
# =====================================================
"F. Giải quyết vấn đề với sự trợ giúp của máy tính":[

{
"question":"Làm việc theo từng bước giúp?",
"options":["Khó hơn","Dễ hoàn thành","Rối hơn"],
"answer":"Dễ hoàn thành"
},

{
"question":"Một việc có thể?",
"options":["Chia nhiều bước","Làm lung tung","Bỏ qua"],
"answer":"Chia nhiều bước"
},

{
"question":"Máy tính giúp?",
"options":["Giải quyết công việc","Đá bóng","Nấu ăn"],
"answer":"Giải quyết công việc"
},

{
"question":"Muốn hoàn thành nhiệm vụ cần?",
"options":["Làm bừa","Bỏ qua","Có kế hoạch"],
"answer":"Có kế hoạch"
},

{
"question":"Sản phẩm là?",
"options":["Chiếc ghế","Kết quả công việc","Cái bàn"],
"answer":"Kết quả công việc"
},

{
"question":"Điều kiện giúp?",
"options":["Ra quyết định","Nghe nhạc","In giấy"],
"answer":"Ra quyết định"
},

{
"question":"Người chỉ huy cần?",
"options":["Nói nhỏ","Không hướng dẫn","Ra lệnh rõ ràng"],
"answer":"Ra lệnh rõ ràng"
},

{
"question":"Nhiệm vụ cần?",
"options":["Rõ ràng","Mơ hồ","Khó hiểu"],
"answer":"Rõ ràng"
},

{
"question":"Máy tính hỗ trợ?",
"options":["Ngủ","Làm việc","Ăn cơm"],
"answer":"Làm việc"
},

{
"question":"Thực hiện đúng các bước giúp?",
"options":["Hoàn thành tốt","Sai nhiều","Không xong"],
"answer":"Hoàn thành tốt"
}

]

}

# =====================================================
# SESSION STATE
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

# =====================================================
# HOME
# =====================================================
if st.session_state.page == "home":

    st.markdown(
        """
        <div class='main-title'>
        💻 HỌC LIỆU SỐ TIN HỌC LỚP 3
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-title'>
        🎮 Học vui - Tương tác - Phát triển năng lực số
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("## 📚 CHỌN CHỦ ĐỀ")

    # ==========================================
    # CÁC NÚT CHỦ ĐỀ
    # ==========================================
    for topic in topics.keys():

        if st.button(topic):

            st.session_state.topic = topic
            st.session_state.page = "quiz"

            st.session_state.question_index = 0
            st.session_state.score = 0

            random.shuffle(topics[topic])

            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# QUIZ
# =====================================================
elif st.session_state.page == "quiz":

    topic_questions = topics[st.session_state.topic]

    total_questions = len(topic_questions)

    progress = st.session_state.question_index / total_questions

    # ==========================================
    # NÚT QUAY LẠI
    # ==========================================
    if st.button("🏠 QUAY VỀ MENU"):

        st.session_state.page = "home"
        st.rerun()

    st.title(st.session_state.topic)

    st.progress(progress)

    # ==========================================
    # ĐIỂM
    # ==========================================
    st.markdown(
        f"""
        <div class='score-box'>
        ⭐ ĐIỂM: {st.session_state.score}/{total_questions}
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==========================================
    # HIỂN THỊ CÂU HỎI
    # ==========================================
    if st.session_state.question_index < total_questions:

        q = topic_questions[st.session_state.question_index]

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.write(
            f"## Câu {st.session_state.question_index + 1}"
        )

        st.write(f"### {q['question']}")

        answer = st.radio(
            "👉 Chọn đáp án:",
            q["options"]
        )

        # ======================================
        # KIỂM TRA
        # ======================================
        if st.button("✅ KIỂM TRA"):

            if answer == q["answer"]:

                st.success("🎉 Chính xác!")

                autoplay_audio("sounds/dung.mp3")

                st.session_state.score += 1

            else:

                st.error(
                    f"❌ Đáp án đúng là: {q['answer']}"
                )

                autoplay_audio("sounds/sai.mp3")

        # ======================================
        # TIẾP THEO
        # ======================================
        if st.button("➡️ CÂU TIẾP THEO"):

            st.session_state.question_index += 1

            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # KẾT THÚC
    # ==========================================
    else:

        autoplay_audio("sounds/finish.mp3")

        st.balloons()

        st.success(
            f"🏆 EM ĐẠT {st.session_state.score}/{total_questions} ĐIỂM"
        )

        # ======================================
        # DANH HIỆU
        # ======================================
        if st.session_state.score <= 4:

            reward = "🌱 CỐ GẮNG THÊM"

        elif st.session_state.score <= 6:

            reward = "⭐ CHĂM HỌC"

        elif st.session_state.score <= 8:

            reward = "🥇 HOÀN THÀNH TỐT"

        elif st.session_state.score == 9:

            reward = "🎖️ XUẤT SẮC"

        else:

            reward = "🏆 SIÊU TIN HỌC"

        st.markdown(
            f"""
            <div class='reward-box'>
            {reward}
            </div>
            """,
            unsafe_allow_html=True
        )

        # ======================================
        # HỘP QUÀ
        # ======================================
        st.write("## 🎁 MỞ HỘP QUÀ")

        if st.button("🎁 NHẬN THƯỞNG"):

            gifts = [
                "🍭 Kẹo ngọt",
                "⭐ 10 sao thưởng",
                "🎮 Một lượt chơi mới",
                "📚 Huy hiệu chăm học"
            ]

            st.success(random.choice(gifts))

        # ======================================
        # LÀM LẠI
        # ======================================
        if st.button("🔄 LÀM LẠI"):

            st.session_state.question_index = 0
            st.session_state.score = 0

            random.shuffle(topic_questions)

            st.rerun()

        # ======================================
        # MENU
        # ======================================
        if st.button("🏠 VỀ MENU CHÍNH"):

            st.session_state.page = "home"

            st.rerun()

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")

st.markdown(
    """
    <div class='footer'>
    🌟 Học liệu số xây dựng bằng Python + Streamlit + AI
    </div>
    """,
    unsafe_allow_html=True
)
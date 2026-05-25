import streamlit as st
import random
import base64

# =====================================================
# CẤU HÌNH TRANG
# =====================================================
st.set_page_config(
    page_title="TH Ngũ Lão_Học liệu số Tin học 3",
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
#MainMenu { visibility:hidden; }
footer{ visibility:hidden; }

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
# DỮ LIỆU CÂU HỎI TIN HỌC LỚP 3
# =====================================================
topics = {
"A. Máy tính và em": [
    {
        "question": "Bộ phận nào của máy tính để bàn giúp em nhập các chữ cái và chữ số vào máy?",
        "options": ["Chuột máy tính", "Bàn phím", "Màn hình"],
        "answer": "Bàn phím"
    },
    {
        "question": "Loại máy tính nào dưới đây có màn hình gắn liền với thân máy, không có bàn phím rời và em có thể dùng ngón tay chạm điều khiển?",
        "options": ["Máy tính để bàn", "Máy tính xách tay (Laptop)", "Máy tính bảng (Tablet)"],
        "answer": "Máy tính bảng (Tablet)"
    },
    {
        "question": "Để mở một thư mục hoặc một phần mềm trên màn hình máy tính, em cần thực hiện thao tác chuột nào?",
        "options": ["Nháy chuột trái một lần", "Nháy đúp chuột (nháy nhanh liên tiếp 2 lần)", "Kéo thả chuột"],
        "answer": "Nháy đúp chuột (nháy nhanh liên tiếp 2 lần)"
    },
    {
        "question": "Khi ngồi học bài với máy tính, khoảng cách an toàn từ mắt em đến màn hình nên là bao nhiêu để bảo vệ thị lực?",
        "options": ["Từ 20 cm đến 30 cm", "Từ 30 cm đến 40 cm", "Từ 50 cm đến 80 cm"],
        "answer": "Từ 50 cm đến 80 cm"
    },
    {
        "question": "Khi đi học, nghe tiếng trống trường vang lên báo giờ ra chơi. Tiếng trống trường thuộc dạng thông tin nào?",
        "options": ["Dạng văn bản", "Dạng hình ảnh", "Dạng âm thanh"],
        "answer": "Dạng âm thanh"
    },
    {
        "question": "Trang sách giáo khoa Tin học có chứa cả chữ viết và hình vẽ minh họa. Trang sách đó cho em biết các dạng thông tin nào?",
        "options": ["Chỉ có dạng âm thanh", "Dạng văn bản và hình ảnh", "Chỉ có dạng văn bản"],
        "answer": "Dạng văn bản và hình ảnh"
    },
    {
        "question": "Trên hàng phím cơ sở, hai phím nào có gờ nổi (gai nhỏ) giúp em đặt hai ngón tay trỏ làm mốc gõ phím?",
        "options": ["Phím F và phím J", "Phím A và phím L", "Phím G và phím H"],
        "answer": "Phím F và phím J"
    },
    {
        "question": "Nếu ngồi học máy tính sai tư thế, quá gần màn hình hoặc ngồi quá lâu, em dễ gặp vấn đề sức khỏe nào dưới đây?",
        "options": ["Bị đau bụng và sâu răng", "Bị cận thị và vẹo cột sống", "Bị ù tai và mỏi chân"],
        "answer": "Bị cận thị và vẹo cột sống"
    },
    {
        "question": "Hàng phím chứa phím Cách (Spacebar) dài nhất nằm ở vị trí nào trên bàn phím máy tính?",
        "options": ["Hàng phím trên", "Hàng phím dưới cùng", "Hàng phím cơ sở"],
        "answer": "Hàng phím dưới cùng"
    },
    {
        "question": "Khi làm một bài toán, phần lệnh \"Đề bài cho biết...\" được coi là gì trong quá trình máy tính hay con người xử lý thông tin?",
        "options": ["Thông tin vào", "Thông tin ra", "Kết quả quyết định"],
        "answer": "Thông tin vào"
    }
],
"B. Mạng máy tính và Internet": [
    {
        "question": "Mạng Internet mang lại lợi ích lớn nhất nào sau đây cho việc học tập của học sinh lớp 3?",
        "options": ["Giúp tự động làm hết bài tập về nhà", "Giúp tìm kiếm thông tin bài học và học trực tuyến", "Giúp máy tính chạy nhanh hơn"],
        "answer": "Giúp tìm kiếm thông tin bài học và học trực tuyến"
    },
    {
        "question": "Khi sử dụng các trang web tìm kiếm, biểu tượng nào thường đại diện cho chức năng \"Tìm kiếm\" thông tin?",
        "options": ["Hình một cuốn sách mở", "Hình một chiếc kính lúp", "Hình một mũi tên xanh"],
        "answer": "Hình một chiếc kính lúp"
    },
    {
        "question": "Để đảm bảo an toàn khi tham gia môi trường mạng Internet, em KHÔNG nên làm điều nào sau đây?",
        "options": ["Xem các video bài học hoạt hình vui nhộn", "Nhắn tin trò chuyện và hẹn gặp mặt người lạ", "Tìm kiếm thông tin về thế giới loài vật"],
        "answer": "Nhắn tin trò chuyện và hẹn gặp mặt người lạ"
    },
    {
        "question": "Trong lúc xem một trang web giải trí, nếu bất ngờ xuất hiện những hình ảnh bạo lực hoặc nội dung làm em sợ hãi, em nên làm gì?",
        "options": ["Tắt ngay trang web đó đi và báo cho bố mẹ hoặc thầy cô biết", "Bấm xem tiếp xem đó là trò gì", "Chia sẻ trang web đó cho các bạn cùng xem"],
        "answer": "Tắt ngay trang web đó đi và báo cho bố mẹ hoặc thầy cô biết"
    },
    {
        "question": "Mạng Internet là gì?",
        "options": ["Là một phần mềm trò chơi cài sẵn trong máy tính", "Là mạng kết nối các máy tính trên toàn thế giới để chia sẻ thông tin", "Là một thiết bị phần cứng cắm vào máy tính"],
        "answer": "Là mạng kết nối các máy tính trên toàn thế giới để chia sẻ thông tin"
    },
    {
        "question": "Thông tin trên mạng Internet có đặc điểm gì mà em cần lưu ý khi sử dụng?",
        "options": ["Tất cả thông tin trên Internet đều đúng tuyệt đối", "Thông tin trên Internet rất đa dạng, nhưng có cả thông tin đúng và thông tin sai", "Trên Internet chỉ có thông tin giả mạo"],
        "answer": "Thông tin trên Internet rất đa dạng, nhưng có cả thông tin đúng và thông tin sai"
    },
    {
        "question": "Thiết bị nào sau đây giúp các máy tính, điện thoại kết nối vào mạng Internet mà không cần cắm dây cáp rườm rà?",
        "options": ["Thiết bị phát sóng WiFi", "Chuột máy tính không dây", "Bộ loa máy tính"],
        "answer": "Thiết bị phát sóng WiFi"
    },
    {
        "question": "Khi nhắn tin trao đổi bài học với bạn bè qua Internet, em cần có thái độ như thế nào là văn minh?",
        "options": ["Sử dụng từ ngữ lịch sự, tôn trọng bạn và không nói tục", "Nói gì cũng được vì không ai nhìn thấy mặt mình", "Trêu chọc, nói xấu hoặc bắt nạt bạn"],
        "answer": "Sử dụng từ ngữ lịch sự, tôn trọng bạn và không nói tục"
    },
    {
        "question": "Để bảo vệ sức khỏe và không ảnh hưởng đến việc học, thời gian em sử dụng Internet hợp lý là:",
        "options": ["Chỉ dùng khi được bố mẹ cho phép và không xem quá lâu liên tục", "Xem bất cứ lúc nào mình thích kể cả ban đêm", "Xem cả ngày vào ngày nghỉ cuối tuần"],
        "answer": "Chỉ dùng khi được bố mẹ cho phép và không xem quá lâu liên tục"
    },
    {
        "question": "Trang web nào dưới đây phù hợp và an toàn để học sinh lớp 3 vừa học vừa chơi?",
        "options": ["Các trang web xem phim hành động, kinh dị", "Các trang web học toán, tiếng Anh trực tuyến dành cho thiếu nhi", "Các diễn đàn tranh luận của người lớn"],
        "answer": "Các trang web học toán, tiếng Anh trực tuyến dành cho thiếu nhi"
    }
],
"C. Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": [
    {
        "question": "Việc sắp xếp sách vở, đồ dùng học tập ngăn nắp, phân loại theo từng môn học trên giá sách sẽ giúp ích gì cho em?",
        "options": ["Làm giá sách nặng hơn", "Giúp em tìm kiếm sách vở nhanh chóng khi cần", "Không có tác dụng gì"],
        "answer": "Giúp em tìm kiếm sách vở nhanh chóng khi cần"
    },
    {
        "question": "Trong máy tính, biểu tượng của Thư mục (Folder) dùng để chứa các tệp dữ liệu thường có hình chiếc kẹp giấy và màu gì?",
        "options": ["Màu xanh lá cây", "Màu đỏ rực", "Màu vàng"],
        "answer": "Màu vàng"
    },
    {
        "question": "Người ta tạo ra các thư mục trong máy tính nhằm mục đích chính là gì?",
        "options": ["Để làm cho máy tính có nhiều màu sắc đẹp hơn", "Để lưu trữ, sắp xếp dữ liệu một cách trật tự và dễ tìm kiếm", "Để bảo vệ máy tính không bị bụi bẩn"],
        "answer": "Để lưu trữ, sắp xếp dữ liệu một cách trật tự và dễ tìm kiếm"
    },
    {
        "question": "Sơ đồ hình cây giúp chúng ta biểu diễn điều gì một cách rõ ràng nhất?",
        "options": ["Cách vẽ một cái cây trong thế giới tự nhiên", "Mối quan hệ phân loại, sắp xếp đồ vật hoặc dữ liệu từ chung đến riêng", "Danh sách các bài hát yêu thích"],
        "answer": "Mối quan hệ phân loại, sắp xếp đồ vật hoặc dữ liệu từ chung đến riêng"
    },
    {
        "question": "Một bức tranh em vẽ bằng phần mềm Paint hoặc một bài thơ em gõ trong máy tính được gọi chung là gì?",
        "options": ["Tệp dữ liệu (File)", "Thư mục (Folder)", "Hệ điều hành"],
        "answer": "Tệp dữ liệu (File)"
    },
    {
        "question": "Mối quan hệ giữa thư mục và tệp dữ liệu trong máy tính giống như hình ảnh nào ngoài đời thực dưới đây?",
        "options": ["Thư mục là chiếc cặp sách, còn tệp dữ liệu là những cuốn sách ở bên trong", "Thư mục là cuốn vở, còn tệp dữ liệu là chiếc bút mực", "Thư mục và tệp dữ liệu hoàn toàn giống nhau"],
        "answer": "Thư mục là chiếc cặp sách, còn tệp dữ liệu là những cuốn sách ở bên trong"
    },
    {
        "question": "Khi đặt tên cho một thư mục mới trong máy tính, em nên đặt tên như thế nào là khoa học?",
        "options": ["Đặt tên thật dài và dùng nhiều ký tự lạ", "Đặt tên ngắn gọn, dễ nhớ và liên quan đến nội dung lưu trữ bên trong", "Không cần đặt tên, để máy tính tự chọn chữ ngẫu nhiên"],
        "answer": "Đặt tên ngắn gọn, dễ nhớ và liên quan đến nội dung lưu trữ bên trong"
    },
    {
        "question": "Cấu trúc cây thư mục trong máy tính cho phép chứa những thành phần nào?",
        "options": ["Chỉ chứa được các tệp dữ liệu", "Chỉ chứa được các thư mục con", "Chứa được các thư mục con và các tệp dữ liệu bên trong"],
        "answer": "Chứa được các thư mục con và các tệp dữ liệu bên trong"
    },
    {
        "question": "Khi muốn xem các tệp dữ liệu hoặc thư mục con ở bên trong một thư mục lớn, em cần thực hiện thao tác nào?",
        "options": ["Nháy đúp chuột vào thư mục lớn đó", "Kéo thả thư mục đó vào thùng rác", "Nháy nút phải chuột rồi chọn Delete"],
        "answer": "Nháy đúp chuột vào thư mục lớn đó"
    },
    {
        "question": "Tất cả thông tin, hình ảnh, bài học mà em lưu trên máy tính sẽ được lưu giữ cố định ở thiết bị nào bên trong máy?",
        "options": ["Bộ nhớ lưu trữ (như Ổ đĩa cứng của máy tính)", "Màn hình hiển thị", "Bàn phím máy tính"],
        "answer": "Bộ nhớ lưu trữ (như Ổ đĩa cứng của máy tính)"
    }
],
"D. Đạo đức, pháp luật và văn hoá trong môi trường số": [
    {
        "question": "Khi đặt mật khẩu cho tài khoản học tập trực tuyến (như tài khoản MS Teams, Zoom hoặc Olm), em nên làm gì?",
        "options": ["Nói cho tất cả các bạn trong lớp cùng biết", "Giữ bí mật mật khẩu, không chia sẻ cho người lạ hoặc bạn bè", "Viết mật khẩu lên bàn học ở lớp"],
        "answer": "Giữ bí mật mật khẩu, không chia sẻ cho người lạ hoặc bạn bè"
    },
    {
        "question": "Những thông tin nào sau đây thuộc về \"Thông tin cá nhân\" mà em cần phải tự bảo vệ, không được tùy tiện công khai trên mạng?",
        "options": ["Họ và tên, địa chỉ nhà, số điện thoại của bố mẹ em", "Tên các loài động vật ăn cỏ", "Danh sách các bài hát có trong máy tính"],
        "answer": "Họ và tên, địa chỉ nhà, số điện thoại của bố mẹ em"
    },
    {
        "question": "Cách đặt mật khẩu nào dưới đây giúp tài khoản máy tính của em an toàn, mạnh và khó bị người khác đoán được?",
        "options": ["Đặt mật khẩu đơn giản như \"123456\" hoặc \"abc\"", "Đặt mật khẩu là chính ngày tháng năm sinh của em", "Kết hợp chữ cái, chữ số và không chứa thông tin quá dễ đoán"],
        "answer": "Kết hợp chữ cái, chữ số và không chứa thông tin quá dễ đoán"
    },
    {
        "question": "Nếu có một người quen trên mạng Internet (nhưng em chưa từng gặp ngoài đời) hẹn gặp em ở công viên, em nên xử lý thế nào?",
        "options": ["Tự ý đạp xe đi gặp họ ngay vì tò mò", "Từ chối thẳng thắn và lập tức kể lại sự việc cho bố mẹ biết", "Rủ thêm một người bạn cùng lớp đi gặp bí mật"],
        "answer": "Từ chối thẳng thắn và lập tức kể lại sự việc cho bố mẹ biết"
    },
    {
        "question": "Tự ý lấy hình ảnh cá nhân của người khác rồi đăng lên mạng Internet khi chưa được sự cho phép của họ là hành vi như thế nào?",
        "options": ["Là hành vi đúng vì mạng Internet là tự do", "Là hành vi không nên làm vì chưa tôn trọng quyền riêng tư của người khác", "Là hành vi đáng khen ngợi"],
        "answer": "Là hành vi không nên làm vì chưa tôn trọng quyền riêng tư của người khác"
    },
    {
        "question": "Khi viết lời bình luận (comment) dưới một bài viết hoặc hình ảnh của bạn mình trên mạng, ngôn ngữ nào là phù hợp?",
        "options": ["Dùng ngôn ngữ lịch sự, vui vẻ, khen ngợi hoặc góp ý chân thành", "Dùng những từ ngữ thô lỗ, chê bai ghét bỏ để trêu chọc bạn", "Nói tục, chửi bậy cho ngầu"],
        "answer": "Dùng ngôn ngữ lịch sự, vui vẻ, khen ngợi hoặc góp ý chân thành"
    },
    {
        "question": "Tại sao việc biết cách bảo vệ thông tin cá nhân khi tham gia môi trường số lại vô cùng quan trọng đối với học sinh?",
        "options": ["Để tránh bị kẻ xấu lợi dụng thông tin để lừa đảo, làm phiền gia đình em", "Để máy tính không bị nhiễm virus", "Để được điểm cao hơn trong môn Tin học"],
        "answer": "Để tránh bị kẻ xấu lợi dụng thông tin để lừa đảo, làm phiền gia đình em"
    },
    {
        "question": "Khi lấy một hình ảnh đẹp trên mạng Internet để đưa vào bài trình chiếu học tập của mình, hành động nào thể hiện sự văn minh?",
        "options": ["Cứ lấy dùng và nói tự mình vẽ ra bức tranh đó", "Chọn hình ảnh phù hợp và ghi chú nguồn gốc (hoặc tên trang web) rõ ràng", "Tải về thật nhiều hình ảnh dù không liên quan đến bài học"],
        "answer": "Chọn hình ảnh phù hợp và ghi chú nguồn gốc (hoặc tên trang web) rõ ràng"
    },
    {
        "question": "Nếu em thấy một bạn học trong lớp mình bị một nhóm người khác chế giễu, bêu rếu bằng những lời lẽ xấu trên mạng xã hội, em nên làm gì?",
        "options": ["Vào hùa tham gia bình luận nói xấu cùng nhóm đó", "Im lặng bỏ qua coi như không biết gì", "Báo ngay với thầy cô chủ nhiệm hoặc cha mẹ để kịp thời giúp đỡ bạn"],
        "answer": "Báo ngay với thầy cô chủ nhiệm hoặc cha mẹ để kịp thời giúp đỡ bạn"
    },
    {
        "question": "Khái niệm \"Môi trường số văn minh và an toàn\" có nghĩa là gì?",
        "options": ["Là nơi mọi người tự do làm bất cứ điều gì mình thích, kể cả cãi nhau", "Là nơi mọi người cư xử lịch sự, tôn trọng lẫn nhau và tuân thủ các quy định an toàn pháp luật", "Là nơi không có ai sử dụng máy tính nữa"],
        "answer": "Là nơi mọi người cư xử lịch sự, tôn trọng lẫn nhau và tuân thủ các quy định an toàn pháp luật"
    }
],
"E. Ứng dụng tin học": [
    {
        "question": "Phần mềm trình chiếu (ví dụ như phần mềm PowerPoint) thường được thầy cô và học sinh dùng để làm gì?",
        "options": ["Để gõ các bài văn dài hàng chục trang", "Để tạo ra các trang chiếu sinh động phục vụ cho việc thuyết trình bài học", "Để tính toán các bảng điểm phức tạp"],
        "answer": "Để tạo ra các trang chiếu sinh động phục vụ cho việc thuyết trình bài học"
    },
    {
        "question": "Trên một trang trình chiếu (được gọi là một Slide), em có thể chèn thêm những loại nội dung nào vào?",
        "options": ["Chỉ chèn được chữ viết thô sơ", "Chèn được cả chữ viết, hình ảnh, âm thanh và các đoạn video", "Chỉ chèn được hình vẽ hình học"],
        "answer": "Chèn được cả chữ viết, hình ảnh, âm thanh và các đoạn video"
    },
    {
        "question": "Phần mềm Mouse Skills thiết kế ra nhằm giúp học sinh lớp 3 rèn luyện kỹ năng nào?",
        "options": ["Kỹ năng gõ bàn phím bằng 10 ngón tay", "Kỹ năng sử dụng thành thạo các thao tác với chuột máy tính", "Kỹ năng vẽ tranh phong cảnh"],
        "answer": "Kỹ năng sử dụng thành thạo các thao tác với chuột máy tính"
    },
    {
        "question": "Khi sử dụng máy tính để xem video quay chậm quá trình một hạt đậu nảy mầm, máy tính đã sử dụng công cụ gì?",
        "options": ["Công cụ đa phương tiện (phối hợp hình ảnh động, âm thanh, video)", "Công cụ tính toán số học", "Công cụ quét virus tự động"],
        "answer": "Công cụ đa phương tiện (phối hợp hình ảnh động, âm thanh, video)"
    },
    {
        "question": "Một bài trình chiếu được coi là đẹp, khoa học và thu hút người xem cần đạt tiêu chuẩn nào dưới đây?",
        "options": ["Có màu nền sặc sỡ, chữ thật nhỏ và chèn kín mít chữ trên một trang", "Màu sắc hài hòa, phông chữ rõ ràng, nội dung ngắn gọn kèm hình ảnh minh họa phù hợp", "Không cần hình ảnh, chỉ cần toàn chữ viết màu đen"],
        "answer": "Màu sắc hài hòa, phông chữ rõ ràng, nội dung ngắn gọn kèm hình ảnh minh họa phù hợp"
    },
    {
        "question": "Trong phần mềm luyện tập thao tác chuột, hành động nhấn giữ nút trái chuột, di chuyển chuột đến vị trí mới rồi thả tay ra gọi là gì?",
        "options": ["Nháy đúp chuột", "Kéo thả chuột", "Nháy nút phải chuột"],
        "answer": "Kéo thả chuột"
    },
    {
        "question": "Việc em chèn thêm những bức ảnh sinh động vào trang trình chiếu bài học đem lại lợi ích gì?",
        "options": ["Làm bài trình chiếu nặng hơn và khó đọc hơn", "Giúp bài trình chiếu trực quan, dễ hiểu, sinh động và hấp dẫn người nghe hơn", "Làm mất thời gian của người xem"],
        "answer": "Giúp bài trình chiếu trực quan, dễ hiểu, sinh động và hấp dẫn người nghe hơn"
    },
    {
        "question": "Việc sử dụng máy tính và internet để khám phá thế giới tự nhiên mang lại lợi ích gì cho học sinh lớp 3?",
        "options": ["Giúp các em quan sát được những hiện tượng kỳ thú của thiên nhiên từ xa mà mắt thường khó nhìn thấy ngay được", "Thay thế hoàn toàn việc ra ngoài thiên nhiên vui chơi", "Làm cho các em lười suy nghĩ hơn"],
        "answer": "Giúp các em quan sát được những hiện tượng kỳ thú của thiên nhiên từ xa mà mắt thường khó nhìn thấy ngay được"
    },
    {
        "question": "Để làm một bài trình chiếu giới thiệu về chủ đề \"Gia đình của em\", trang đầu tiên (trang tiêu đề) em nên viết nội dung gì?",
        "options": ["Tên bài trình chiếu và họ tên của em (người làm bài)", "Danh sách các món ăn yêu thích của gia đình", "Lời cảm ơn thầy cô đã lắng nghe"],
        "answer": "Tên bài trình chiếu và họ tên của em (người làm bài)"
    },
    {
        "question": "Học môn Tin học và làm quen với máy tính từ sớm giúp ích gì cho hành trình học tập tương lai của em?",
        "options": ["Giúp em sử dụng công nghệ thông minh, an toàn để phục vụ việc tự học và tìm kiếm tri thức", "Để em có thể chơi trò chơi điện tử suốt ngày", "Để không phải học các môn học khác nữa"],
        "answer": "Giúp em sử dụng công nghệ thông minh, an toàn để phục vụ việc tự học và tìm kiếm tri thức"
    }
],
"F. Giải quyết vấn đề với sự trợ giúp của máy tính": [
    {
        "question": "Khi gặp một công việc lớn hoặc một bài toán khó, việc chia nhỏ công việc đó thành các bước thực hiện lần lượt từ trên xuống dưới gọi là gì?",
        "options": ["Làm việc tùy hứng", "Làm việc theo từng bước", "Bỏ qua không làm nữa"],
        "answer": "Làm việc theo từng bước"
    },
    {
        "question": "Bạn An nói: \"Nếu sáng mai trời mưa thì em sẽ đi học bằng áo mưa, nếu trời không mưa thì em đi bộ\". Việc chọn trang phục đi học của An phụ thuộc vào điều gì?",
        "options": ["Phụ thuộc vào sở thích của bạn An", "Phụ thuộc vào điều kiện thời tiết thực tế", "Phụ thuộc vào giờ giấc báo thức"],
        "answer": "Phụ thuộc vào điều kiện thời tiết thực tế"
    },
    {
        "question": "Để trở thành một \"người chỉ huy giỏi\" khi hướng dẫn các bạn làm một việc nhóm, em cần đưa ra các bước lệnh như thế nào?",
        "options": ["Đưa ra các bước lệnh rõ ràng, ngắn gọn, dễ hiểu và đúng thứ tự thực hiện", "Nói thật to nhưng các bước lộn xộn", "Không cần hướng dẫn, để các bạn tự làm bừa"],
        "answer": "Đưa ra các bước lệnh rõ ràng, ngắn gọn, dễ hiểu và đúng thứ tự thực hiện"
    },
    {
        "question": "Trước khi bắt tay vào thực hiện một nhiệm vụ học tập trên máy tính, bước đầu tiên quan trọng nhất em cần xác định là gì?",
        "options": ["Xác định rõ nhiệm vụ cần làm là gì và kết quả (sản phẩm) mong muốn thu được", "Bấm lung tung các nút trên máy tính xem có gì xảy ra", "Chuẩn bị sẵn đồ ăn nhẹ cạnh máy tính"],
        "answer": "Xác định rõ nhiệm vụ cần làm là gì và kết quả (sản phẩm) mong muốn thu được"
    },
    {
        "question": "Khi em dùng phần mềm Word để gõ hoàn chỉnh một bài thơ tặng mẹ và lưu vào máy tính, bài thơ được lưu đó gọi là gì?",
        "options": ["Là điều kiện thực hiện", "Là sản phẩm của nhiệm vụ", "Là lệnh chỉ huy"],
        "answer": "Là sản phẩm của nhiệm vụ"
    },
    {
        "question": "Máy tính có thể tự động làm hết mọi bài tập, mọi công việc thay con người mà không cần chúng ta ra lệnh hay hướng dẫn không?",
        "options": ["Có, máy tính thông minh hơn con người rất nhiều", "Không, máy tính chỉ là công cụ thực hiện theo các bước lệnh do con người thiết kế và chỉ huy", "Máy tính chỉ tự làm việc vào ban đêm"],
        "answer": "Không, máy tính chỉ là công cụ thực hiện theo các bước lệnh do con người thiết kế và chỉ huy"
    },
    {
        "question": "Điều gì sẽ xảy ra nếu em thực hiện sai thứ tự các bước trong quy trình pha một ly sữa nóng (ví dụ: cho sữa đặc vào trước, đổ nước nguội vào thay vì nước nóng)?",
        "options": ["Sữa vẫn thơm ngon như bình thường", "Sữa không tan hết và kết quả không đạt như mong muốn", "Máy tính sẽ báo lỗi ngay lập tức"],
        "answer": "Sữa không tan hết và kết quả không đạt như mong muốn"
    },
    {
        "question": "Để giúp bố mẹ dọn dẹp nhà cửa sạch sẽ theo từng bước logic, bước nào dưới đây nên được thực hiện trước tiên?",
        "options": ["Dùng chổi quét sạch rác và bụi trên sàn nhà", "Dùng cây lau nhà ướt để lau sàn", "Bật quạt cho sàn nhà mau khô"],
        "answer": "Dùng chổi quét sạch rác và bụi trên sàn nhà"
    },
    {
        "question": "Khi gặp một bài toán tính nhẩm có dãy số rất dài và phức tạp, em có thể tìm sự trợ giúp từ phần mềm tiện ích nào có sẵn trên máy tính?",
        "options": ["Phần mềm luyện gõ bàn phím", "Phần mềm máy tính bỏ túi (Calculator)", "Phần mềm vẽ tranh Paint"],
        "answer": "Phần mềm máy tính bỏ túi (Calculator)"
    },
    {
        "question": "Việc hình thành thói quen lên kế hoạch và làm việc theo từng bước rõ ràng sẽ đem lại lợi ích gì cho em?",
        "options": ["Giúp công việc được giải quyết chính xác, hiệu quả và dễ thành công hơn", "Làm cho em mất nhiều thời gian vui chơi hơn", "Làm cho công việc trở nên rắc rối hơn"],
        "answer": "Giúp công việc được giải quyết chính xác, hiệu quả và dễ thành công hơn"
    }
]
}

# =====================================================
# INITIALIZE SESSION STATE
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "current_questions" not in st.session_state:
    st.session_state.current_questions = []

# =====================================================
# HOME PAGE
# =====================================================
if st.session_state.page == "home":
    st.markdown("<div class='main-title'>💻 HỌC LIỆU SỐ TIN HỌC LỚP 3</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>🎮 Học vui - Tương tác - Phát triển năng lực số</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.write("## 📚 CHỌN CHỦ ĐỀ")

    for topic in topics.keys():
        if st.button(topic):
            st.session_state.topic = topic
            st.session_state.page = "quiz"
            st.session_state.question_index = 0
            st.session_state.score = 0
            
            # Đảo và lưu bản sao câu hỏi vào session_state riêng biệt
            shuffled_list = list(topics[topic])
            random.shuffle(shuffled_list)
            st.session_state.current_questions = shuffled_list
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# QUIZ PAGE
# =====================================================
elif st.session_state.page == "quiz":
    topic_questions = st.session_state.current_questions
    total_questions = len(topic_questions)
    
    if st.button("🏠 QUAY VỀ MENU"):
        st.session_state.page = "home"
        st.rerun()

    st.title(st.session_state.topic)
    
    # Tính toán thanh tiến trình an toàn
    progress = min(st.session_state.question_index / total_questions, 1.0)
    st.progress(progress)

    st.markdown(f"<div class='score-box'>⭐ ĐIỂM: {st.session_state.score}/{total_questions}</div>", unsafe_allow_html=True)

    if st.session_state.question_index < total_questions:
        q = topic_questions[st.session_state.question_index]
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.write(f"## Câu {st.session_state.question_index + 1}")
        st.write(f"### {q['question']}")

        # Thêm key duy nhất dựa trên index câu hỏi để tránh lưu đáp án cũ từ câu trước
        answer = st.radio("👉 Chọn đáp án:", q["options"], key=f"q_{st.session_state.question_index}")

        col1, col2 = st.columns(2)
        with col1:
            btn_kiem_tra = st.button("✅ KIỂM TRA", use_container_width=True)
        with col2:
            btn_tiep_theo = st.button("➡️ CÂU TIẾP THEO", use_container_width=True)

        if btn_kiem_tra:
            if answer == q["answer"]:
                st.success("🎉 Chính xác!")
                autoplay_audio("dung.mp3")
                st.session_state.score += 1
            else:
                st.error(f"❌ Đáp án đúng là: {q['answer']}")
                autoplay_audio("sai.mp3")

        if btn_tiep_theo:
            st.session_state.question_index += 1
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # KẾT THÚC VÀ KHEN THƯỞNG
    # ==========================================
    else:
        autoplay_audio("finish.mp3")
        st.balloons()
        st.success(f"🏆 EM ĐẠT {st.session_state.score}/{total_questions} ĐIỂM")

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

        st.markdown(f"<div class='reward-box'>{reward}</div>", unsafe_allow_html=True)
        st.write("## 🎁 MỞ HỘP QUÀ")

        if st.button("🎁 NHẬN THƯỞNG"):
            gifts = ["🍭 Kẹo ngọt", "⭐ 10 sao thưởng", "🎮 Một lượt chơi mới", "📚 Huy hiệu chăm học"]
            st.success(random.choice(gifts))

        # ĐÃ SỬA LỖI ĐẢO ĐÁP ÁN KHI LÀM LẠI
        if st.button("🔄 LÀM LẠI"):
            st.session_state.question_index = 0
            st.session_state.score = 0
            
            # Lấy bộ câu hỏi gốc thuộc chủ đề hiện tại để đảo mới hoàn toàn
            shuffled_list = list(topics[st.session_state.topic])
            random.shuffle(shuffled_list)
            st.session_state.current_questions = shuffled_list
            st.rerun()

        if st.button("🏠 VỀ MENU CHÍNH"):
            st.session_state.page = "home"
            st.rerun()
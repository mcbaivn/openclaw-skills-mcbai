import sys, json, re

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

with open(r'C:\Users\PCM\.openclaw\workspace\srt_clean.json', encoding='utf-8') as f:
    data = json.load(f)

# Manual translation (Chinese Traditional -> Vietnamese)
translations = {
    1: "Khách hàng",
    2: "Chào mừng",
    3: "Bạn có thấy tôi đẹp không?",
    4: "Ờ...",
    5: "Xấu kinh khủng",
    6: "Không sao đâu",
    7: "Tiệm tôi tinh thông kỹ thuật thẩm mỹ",
    8: "Cứ để tôi lo",
    9: "Tôi",
    10: "Tin tưởng anh",
    11: "Yên tâm đi",
    12: "Tôi đã làm tóc cho Sadako",
    13: "Khâu vết thương cho Alien",
    14: "Và phẫu thuật tạo hình cho hơn tám mươi người",
    15: "Giờ có thể bắt đầu ca mổ",
    16: "Đây là một thế giới cổ tích tăm tối",
    17: "Nơi ngập tràn những nỗi kinh hoàng chưa biết",
    18: "Hiện tại",
    19: "Do là cái nhìn về thế giới cổ tích tăm tối này",
    20: "Bác sĩ",
    21: "Gặp gỡ vô số yêu ma quỷ quái",
    22: "Và tất cả những điều này",
    23: "Đều bắt đầu từ",
    24: "Tiệm thuốc nhỏ bé kia",
    25: "Ra ngoài phải mang đèn",
    26: "Không được đi xa",
    27: "Cách cổng mười mét trở ra",
    28: "Bóng tối bên ngoài sẽ nuốt chửng anh",
    29: "Dù người đến khám là người",
    30: "Hay ma",
    31: "Hay quái vật phun độc",
    32: "Đều phải giữ bình tĩnh",
    33: "Đến giờ rồi",
    34: "Treo đèn ra ngoài đi",
    35: "Chuẩn bị mở cửa kinh doanh",
    36: "Có người rồi",
    37: "Giáo viên của anh",
    38: "Kẻ Cuồng Máu",
    39: "Giao nhiệm vụ cho anh",
    40: "Mở cửa kinh doanh",
    41: "Phần thưởng hoàn thành nhiệm vụ",
    42: "Thức ăn xương sọ",
    43: "Kinh nghiệm cơ bản nhân năm",
    44: "Máu người tinh khiết nhân một trăm ml",
    45: "Nhanh lên nào",
    46: "Anh nhận được",
    47: "Thức ăn xương sọ",
    48: "Kinh nghiệm cơ bản nhân năm",
    49: "Máu người tinh khiết nhân một trăm ml",
    50: "Cậu bé ơi",
    51: "Chào buổi sáng",
    52: "Cậu có thứ gì không còn dùng nữa không",
    53: "Cho bà lão này với",
    54: "Bà sẽ trả công xứng đáng cho cậu",
    55: "Kẻ thu nhặt da người"
}

# Build translated list
translated = []
for item in data:
    translated.append({
        "id": item["id"],
        "timecode": item["timecode"],
        "text": translations.get(item["id"], item["text"])
    })

# Build SRT content
srt_lines = []
for item in translated:
    srt_lines.append(str(item["id"]))
    srt_lines.append(item["timecode"])
    srt_lines.append(item["text"])
    srt_lines.append("")

srt_content = "\n".join(srt_lines)

out_path = r'C:\Users\PCM\.openclaw\workspace\subtitle_vi.srt'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(srt_content)

print(f"Done! Saved to: {out_path}")
print(f"Total: {len(translated)} subtitles translated")

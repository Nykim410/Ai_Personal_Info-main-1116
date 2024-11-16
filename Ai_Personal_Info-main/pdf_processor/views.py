# pdf_processor/views.py
import pdfplumber
import openai
from django.shortcuts import render, redirect
from django.conf import settings
from .models import PolicyDocument
from .forms import PolicyDocumentForm
from pdf_processor import views


# OpenAI API 키 설정
openai.api_key = "YOUR_OPENAI_API_KEY"

# PDF에서 텍스트 추출 함수
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# OpenAI API를 이용한 정책 분석 함수
def analyze_policy(text):
    prompt = (
        f"다음 정책 문서의 내용을 요약하고 주요 변경 사항이 컴플라이언스에 미치는 영향을 분석해 주세요:\n\n{text}"
    )
    response = openai.Completion.create(
        engine="gpt-4",  # GPT 모델 사용
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

# PDF 업로드 및 분석 뷰
def upload_and_analyze_pdf(request):
    if request.method == 'POST':
        form = PolicyDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            policy_doc = form.save()  # 모델에 PDF 파일 저장
            # PDF에서 텍스트 추출
            text = extract_text_from_pdf(policy_doc.file.path)
            # OpenAI를 사용한 분석 수행
            analysis_result = analyze_policy(text)
            policy_doc.analysis_result = analysis_result
            policy_doc.save()
            return redirect('analysis_result', pk=policy_doc.pk)
    else:
        form = PolicyDocumentForm()
    return render(request, 'pdf_processor/upload_pdf.html', {'form': form})

# 분석 결과 뷰
def analysis_result(request, pk):
    policy_doc = PolicyDocument.objects.get(pk=pk)
    return render(request, 'pdf_processor/analysis_result.html', {'policy_doc': policy_doc})

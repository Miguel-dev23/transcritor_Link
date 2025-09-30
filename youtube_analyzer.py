import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extrai o ID do vídeo da URL do YouTube"""
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    elif 'youtube.com' in url:
        parsed = urlparse(url)
        return parse_qs(parsed.query).get('v', [None])[0]
    return None

def get_transcript(video_id):
    """Obtém a transcrição do vídeo"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        return ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Erro ao obter transcrição: {e}")
        return None

def summarize_with_ai(text):
    """Usa IA para resumir o texto"""
    # Simula chamada para API de IA (substitua pela sua API preferida)
    # Exemplo com OpenAI ou similar
    prompt = f"Resuma este texto em 3-5 pontos principais:\n\n{text[:4000]}"
    
    # Para demonstração, retorna um resumo básico
    sentences = text.split('.')[:10]
    return f"Resumo do vídeo:\n• " + "\n• ".join(sentences[:5])

def analyze_youtube_video(url):
    """Função principal que analisa o vídeo do YouTube"""
    print(f"Analisando vídeo: {url}")
    
    # Extrai ID do vídeo
    video_id = extract_video_id(url)
    if not video_id:
        return "URL inválida do YouTube"
    
    # Obtém transcrição
    transcript = get_transcript(video_id)
    if not transcript:
        return "Não foi possível obter a transcrição do vídeo"
    
    # Gera resumo
    summary = summarize_with_ai(transcript)
    return summary

# Exemplo de uso
if __name__ == "__main__":
    url = input("Digite a URL do vídeo do YouTube: ")
    result = analyze_youtube_video(url)
    print("\n" + "="*50)
    print(result)

"""Transcreva qualquer audio na sua maquina, de graca, com timestamps.

Usa o faster-whisper, uma reimplementacao do Whisper da OpenAI que roda ate
4x mais rapido em CPU. Nada sai do seu computador.

    pip install faster-whisper
    python main.py reuniao.mp3
"""
import sys

from faster_whisper import WhisperModel

# "small" e o equilibrio: 460 MB, portugues bom, roda em CPU comum.
# Troque por "medium" ou "large-v3" se tiver GPU.
MODELO = "small"


def formatar(segundos):
    m, s = divmod(int(segundos), 60)
    return f"{m:02d}:{s:02d}"


def transcrever(caminho):
    modelo = WhisperModel(MODELO, device="cpu", compute_type="int8")
    segmentos, info = modelo.transcribe(caminho, language="pt",
                                        vad_filter=True)
    print(f"idioma: {info.language}  duracao: {formatar(info.duration)}\n")
    for seg in segmentos:
        print(f"[{formatar(seg.start)} -> {formatar(seg.end)}] {seg.text.strip()}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("uso: python main.py audio.mp3")
    transcrever(sys.argv[1])

# Transcrição com Whisper, na sua máquina

Transcreve áudio em português com timestamps, de graça e offline, usando o
`faster-whisper`.

```
pip install faster-whisper
python main.py reuniao.mp3
```

- O modelo `small` (460 MB) baixa na primeira execução e fica em cache.
- `vad_filter=True` pula os trechos de silêncio, o que acelera e evita
  alucinação em pausas longas.
- `compute_type="int8"` é o modo leve para CPU. Com GPU NVIDIA, use
  `device="cuda"` e `compute_type="float16"`.

Aceita mp3, wav, m4a, ogg e vídeo (o áudio é extraído pelo ffmpeg embutido).

Publicado pelo [@python_brasil](https://instagram.com/python_brasil).

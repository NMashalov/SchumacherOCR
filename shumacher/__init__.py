from huggingface_hub import hf_hub_url, cached_download

MODELS = {
    'ruNoughat': dict(
        repo_id='ai-forever/ruclip-vit-base-patch32-224',
        filenames=[
            'bpe.model', 'config.json', 'pytorch_model.bin'
        ]
    ),  

}


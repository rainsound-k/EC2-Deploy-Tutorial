# EC2 Deploy project
AWS의 EC2 배포를 연습하는 프로젝트입니다.
`.secrets`폴더내의 파일로 비밀 키를 관리합니다.

## requirements

- Python (3.6)

## Installation
```
pip install -r requirements.txt
```
## Secrets

**`.secrets/base.json`**
```json
{
   "SECRET_KEY": "<Django settings SECRET_KEY value>"
}
```
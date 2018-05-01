# EC2 Deploy project

AWS의 EC2 배포를 연습하는 프로젝트입니다.
`.secrets`폴더내의 파일로 비밀 키를 관리합니다.

DB로 PostgreSQL을 사용하며, `local`환경에서는 `localhost`의 DB, `dev`환경과 `production`환경에서는 `AWS RDS`의 DB를 사용합니다.

## 환경 구분

### local

외부 서비스 접근 없이 개발 환경만을 사용 (DB와 Storage를 전부 로컬환경에서 구성)

### dev

DB, Storage에 외부 서비스 (AWS RDS, S3)를 사용

### production

실제 배포 환경

## Requirements

- Python (3.6)
- PostgreSQL

## Installation

```
pip install -r requirements.txt
```

## Secrets

**`.secrets/base.json`**

`RAVEN_DSN`: Sentry의 SecurityToken

```json
{
  "SECRET_KEY": "<Django settings SECRET_KEY value>",
  "RAVEN_DSN": "https://<SecurityToekn>@sentry.io/..."
}
```

**`.secrets/local.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "localhost",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": "<Port number, default:5432>"
    }
  }
}
```

**`.secrets/dev.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<자신의 RDS주소>",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": "<Port number, default:5432>"
    }
  }
}
```

**`.secrets/production.json`**

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<자신의 RDS주소>",
      "NAME": "<DB name>",
      "USER": "<DB username>",
      "PASSWORD": "<DB user password>",
      "PORT": "<Port number, default:5432>"
    }
  }
}
```
# Algo Dungeon

Gamified algorithmic problem-solving platform.

---

## 🏛️ Architecture Overview

- **Frontend**: React + TypeScript + Vite + Tailwind CSS + CodeMirror (Port 5173 / Port 80)
- **Backend**: Python 3.12 + FastAPI + SQLAlchemy 2.0 (asyncpg) + Uvicorn + Pydantic (Port 8000)
- **Database**: PostgreSQL 16 Alpine with persistent Docker volume (Port 5432)
- **Orchestration**: Docker Compose with bridged networking (`app-network`) and live code reloading

---

## 🐳 Getting Started with Docker Compose

### 1. Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/) (v20+)
- [Docker Compose](https://docs.docker.com/compose/) (v2+)

### 2. Environment Configuration

Copy the example environment file:

```bash
cp .env.example .env
```

### 3. Launch Development Stack

Run all containers (Frontend + Backend + PostgreSQL):

```bash
docker compose up
```

Or run detached in the background:

```bash
docker compose up -d
```

### 4. Service URLs & Ports

| Service | URL | Description |
| :--- | :--- | :--- |
| **Frontend** | [http://localhost:5173](http://localhost:5173) | Vite React App with live Hot Module Replacement (HMR) |
| **Backend API** | [http://localhost:8000](http://localhost:8000) | FastAPI REST API |
| **Interactive API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | Swagger UI for testing API endpoints |
| **API Health Check** | [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health) | Reports status of API & PostgreSQL connection |
| **Database** | `localhost:5432` | PostgreSQL 16 database |

> **Note on Vite Proxy**: The frontend dev server proxies all `/api/*` requests seamlessly to `http://backend:8000`. You can test this in your browser at [http://localhost:5173/api/v1/health](http://localhost:5173/api/v1/health).

To shut down the entire stack:

```bash
docker compose down
```

---

## 🔌 API Endpoints Summary

### Health
- `GET /api/v1/health`: Checks application and PostgreSQL connection status.

### Hero Authentication & Conquered Trials
- `POST /api/v1/auth/signup`: Summon an adventurer using `hero_name` (Player Call-Sign) and `secret_incantation` (Password). Zero verification / OTP required.
- `POST /api/v1/auth/login`: Unlock citadel gates with your `hero_name` and `secret_incantation`.
- `GET /api/v1/auth/me`: Retrieve active adventurer profile, level, XP, and conquered problems list.
- `POST /api/v1/auth/passed-problems`: Mark a problem as conquered/passed (`{"problem_id": "two-sum"}`).
- `GET /api/v1/auth/passed-problems`: List all conquered problem IDs.
- `DELETE /api/v1/auth/passed-problems/{problem_id}`: Unmark a problem to allow replaying.

### Submissions
- `POST /api/v1/submissions`: Saves code submission results (problem ID, language, code, test results, execution time).
- `GET /api/v1/submissions`: Lists recent submissions with pagination (`limit`, `offset`) and filter by `problem_id`.
- `GET /api/v1/submissions/{id}`: Fetches details for a specific submission.

### User Progress
- `GET /api/v1/progress/{handle}`: Gets or creates player progress (level, XP, dungeon floor, solved problems).
- `POST /api/v1/progress/{handle}`: Updates player XP, level, dungeon floor, and adds completed problems.

---

## 🚀 Production Mode (Nginx Frontend)

To test or deploy the production build served by Nginx:

```bash
docker compose -f docker-compose.prod.yml up --build -d
```

- **URL:** [http://localhost](http://localhost) (Port 80)
- Single Page Application routing (`/` fallback to `index.html`)
- Gzip compression and static asset caching enabled
- Dynamic reverse proxy for `/api/` upstream

To stop the production container:

```bash
docker compose -f docker-compose.prod.yml down
```

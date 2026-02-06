# Nutzen der Node-Version, die zu deinem Projekt passt (Node 20 ist aktuell Standard)
FROM --platform=$BUILDPLATFORM node:20-slim

WORKDIR /app

# 1. Nur die Package-Dateien kopieren (nutzt Docker-Caching für npm install)
COPY package*.json ./

# 2. Abhängigkeiten installieren
RUN npm install

# 3. Den restlichen Code kopieren
COPY . .

# Vite Standard-Port
EXPOSE 5173

# Startbefehl: --host ist EXTREM wichtig, damit du vom Mac auf den Container zugreifen kannst
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
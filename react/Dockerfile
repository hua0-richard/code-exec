FROM node:16

WORKDIR /react

COPY package*.json ./

RUN npm i

COPY . .

ENV PORT=5173

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]




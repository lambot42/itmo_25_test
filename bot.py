from fastapi import FastAPI, Request
import uvicorn
from parser import get_courses

# Парсим учебные планы при запуске (можно закешировать при необходимости)
courses_ai = get_courses("https://abit.itmo.ru/program/master/ai")
courses_ai_product = get_courses("https://abit.itmo.ru/program/master/ai_product")

app = FastAPI()

def recommend_courses(courses, background):
    recs = []
    for course in courses:
        cl = course.lower()
        if 'программ' in background and ("машинное обучение" in cl or "искусственный интеллект" in cl):
            recs.append(course)
        elif 'бизнес' in background and ("управление продуктом" in cl or "предприниматель" in cl):
            recs.append(course)
        elif 'data' in background and "data" in cl:
            recs.append(course)
    return recs or courses[:3]

@app.post("/webhook")
async def vk_bot(request: Request):
    data = await request.json()
    message = data.get('object', {}).get('text', '').lower()

    if 'ai product' in message:
        selected_courses = courses_ai_product
        program = 'AI Product'
    elif 'ai' in message:
        selected_courses = courses_ai
        program = 'AI'
    else:
        return {"text": "Выберите интересующую программу: AI или AI Product. Я помогу с планом и советом по дисциплинам."}

    if 'план' in message:
        answer = f"Учебный план {program}:\n" + '\n'.join(selected_courses[:5]) + '\n...'
    elif 'выборные' in message or 'рекомендац' in message or 'дисциплин' in message:
        if "программ" in message:
            bg = "программ"
        elif "бизнес" in message:
            bg = "бизнес"
        elif "data" in message:
            bg = "data"
        else:
            return {"text": "Уточните ваш бэкграунд: программирование, бизнес или data?"}
        recs = recommend_courses(selected_courses, bg)
        answer = f"Для вашего профиля советую:\n" + '\n'.join(recs[:5])
    elif 'чем отличается' in message or 'разница' in message:
        answer = ("AI — про исследование ИИ, машинное обучение, глубокие алгоритмы.\n"
                  "AI Product — про запуск ИИ-продуктов, управление и бизнес-подходы.")
    else:
        answer = "Я могу отвечать только на вопросы по программам AI и AI Product магистратуры ИТМО."

    return {"text": answer}

if __name__ == "__main__":
    uvicorn.run("bot:app", host="0.0.0.0", port=8000)
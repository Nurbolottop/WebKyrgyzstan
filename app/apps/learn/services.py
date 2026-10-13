import random

from apps.base.images import renditions


def image_src(image, width=960):
    variants = renditions(image)
    for url, w in variants:
        if w >= width:
            return url
    return variants[-1][0] if variants else ''


def question_payload(question, shuffle=True):
    answers = [{'text': a.text, 'correct': a.is_correct} for a in question.answers.all()]
    if shuffle:
        random.shuffle(answers)
    return {
        'text': question.text,
        'image': image_src(question.image),
        'imageAlt': question.image_alt,
        'explanation': question.explanation,
        'answers': answers,
    }


def quiz_payload(quiz):
    questions = quiz.questions.prefetch_related('answers')
    return {
        'id': quiz.slug,
        'title': quiz.title,
        'questions': [question_payload(q, quiz.shuffle_answers) for q in questions if q.answers.all()],
    }

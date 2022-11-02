
END_COMMAND: str = 'end'

NEXT_COMMAND_BY_PREV_COMMAND = {
    'issue_name': 'issue_type',
    'issue_type': 'issue_priority',
    'issue_priority': 'end',
    'end': 'stop',
    'stop': 'stop',
}

BOT_RESPONSE_BY_NEXT_COMMAND = {
    'issue_name': 'Название',
    'issue_type': 'Тип',
    'issue_priority': 'Приоритет',
    'end': 'Готово',
    'stop': 'Отвали или создавай еще через /create',
}


__all__ = (
    'END_COMMAND',
    'NEXT_COMMAND_BY_PREV_COMMAND',
    'BOT_RESPONSE_BY_NEXT_COMMAND',
)

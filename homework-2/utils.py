def recalculate_avg(*, old_avg: float, new_value: float, old_avg_elements_count: int) -> float:
    """
    Выполняет перерасчет среднего значения.
    Args:
        old_avg: float, старое среднее значение.
        new_value: float, новое значение которое добавляется к old_avg и
            из-за которого выполняется перерасчет.
        old_avg_elements_count: количество элементов, которые участвовали в
            старом среднем значении.

    Returns:
        float: новое среднее значение.
    """
    return (old_avg + new_value) / (old_avg_elements_count + 1) \
        if old_avg_elements_count != 0 else new_value

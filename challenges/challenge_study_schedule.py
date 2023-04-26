def study_schedule(permanence_periods, target_time):
    if target_time is None:
        return None

    number_of_students_present_at_target_time = 0

    for start_of_permanence, end_of_permanence in permanence_periods:
        if (
            start_of_permanence is None
            or end_of_permanence is None
            or not isinstance(start_of_permanence, int)
            or not isinstance(end_of_permanence, int)
        ):
            return None

        if start_of_permanence <= target_time <= end_of_permanence:
            number_of_students_present_at_target_time += 1

    return number_of_students_present_at_target_time


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# # target_time = 5  # saída: 3
# # target_time = 4  # saída: 3
# # target_time = 3  # saída: 2
# target_time = 2  # saída: 4
# # target_time = 1  # saída: 2

# Para esse exemplo, depois de rodar a função para todos esses `target_times'
# julgamos que o melhor horário é o `2`, pois esse retornou `4`,
# já que 4 estudantes estavam presentes nesse horário!


# if __name__ == "__main__":
#     result = study_schedule(permanence_period, target_time)
#     print(result)

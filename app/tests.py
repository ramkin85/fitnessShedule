from django.test import TestCase

# Create your tests here.

from datetime import date

d = date()
s
SELECT `shedule_lesson`.`id`, `shedule_lesson`.`StartDate`, `shedule_lesson`.`EndDate`, `shedule_lesson`.`DayOfWeek`, `shedule_lesson`.`Type`, `shedule_lesson`.`StartTime`, `shedule_lesson`.`EndTime`, `shedule_lesson`.`Trainer_id`, `shedule_lesson`.`PlacesCount`, `shedule_lesson`.`Active` FROM `shedule_lesson` WHERE (`shedule_lesson`.`Active` = True AND `shedule_lesson`.`StartDate` <= 1454187599 AND `shedule_lesson`.`EndDate` >= 1453582800)
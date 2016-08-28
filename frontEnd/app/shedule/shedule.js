'use strict';

angular.module('trainingShedule.shedule', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/shedule', {
            templateUrl: 'shedule/shedule.html',
            controller: 'SheduleCtrl'
        });
    }])

    .controller('SheduleCtrl', ['$scope', 'Service', function ($scope, Service) {

        $scope.objectName = 'lesson';
        $scope.defaultMode = 'shedule';
        $scope.mode = $scope.defaultMode;
        $scope.currentWeekDay = moment();
        $scope.lessonDefaultState = {
            Type: 'group',
            dateRange: {startDate: null, endDate: null},
            StartTime: moment().unix(),
            EndTime: moment().unix()
        };
        $scope.currentLesson = $scope.lessonDefaultState;
        $scope.DAY_LIST = [
            {id: 0, name: 'Пн'},
            {id: 1, name: 'Вт'},
            {id: 2, name: 'Ср'},
            {id: 3, name: 'Чт'},
            {id: 4, name: 'Пт'},
            {id: 5, name: 'Сб'},
            {id: 6, name: 'Вс'}
        ];
        $scope.TIME_LIST = [
            '10:00:00',
            '11:00:00',
            '12:00:00',
            '13:00:00',
            '14:00:00',
            '15:00:00',
            '16:00:00',
            '17:00:00',
            '18:00:00'
        ];
        $scope.dateRangeOptions = {
            locale: {
                format: 'DD.MM.YYYY',
                cancelLabel: 'Отменить',
                applyLabel: 'Выбрать',
                daysOfWeek: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
                monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
                firstDay: 0
            }
        };
        $scope.weekShedule = [
            {
                day: 'monday', lessons: [
                {
                    day: 'monday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'monday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'monday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'monday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'tuesday', lessons: [
                {
                    day: 'tuesday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'tuesday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'tuesday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'tuesday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'wednesday', lessons: [
                {
                    day: 'wednesday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'wednesday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'wednesday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'wednesday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'thursday', lessons: [
                {
                    day: 'thursday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'thursday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'thursday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'thursday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'friday', lessons: [
                {
                    day: 'friday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'friday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'friday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'friday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'saturday', lessons: [
                {
                    day: 'saturday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'saturday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'saturday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'saturday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            },
            {
                day: 'sunday', lessons: [
                {
                    day: 'sunday',
                    time: '10.00-11.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '11.00-12.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'sunday',
                    time: '12.00-13.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '13.00-14.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '14.00-15.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'group'
                },
                {
                    day: 'sunday',
                    time: '15.00-16.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '16.00-17.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '17.00-18.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                },
                {
                    day: 'sunday',
                    time: '18.00-19.00',
                    lesson: 'Вера Маркелова',
                    maxCount: 6,
                    freePlaces: 3,
                    type: 'individual'
                }
            ]
            }
        ];

        var getCurrentWeek = function () {
            var startDate = $scope.currentWeekDay.startOf('WEEK').format('DD.MM.YYYY');
            var endDate = $scope.currentWeekDay.endOf('WEEK').format('DD.MM.YYYY');
            $scope.selectedWeek = startDate+' - '+endDate;
        };
        $scope.changeWeek = function(direction){
            if (direction<0){
                $scope.currentWeekDay = $scope.currentWeekDay.subtract(direction*-1, 'weeks')
            } else {
                $scope.currentWeekDay = $scope.currentWeekDay.add(direction, 'weeks')
            }
            getCurrentWeek();
            $scope.getList();
        };

        $scope.bindClientToClass = function (lesson) {
            $scope.currentLesson = lesson;
            $scope.mode = 'bindClientToLesson';
            $scope.getCurrentLessonString('Запись на занятие. ');
        };
        $scope.vote = function (day, time) {
            var startTime = moment().hours(time.substr(0,2)).minutes(time.substr(3,2));
            var endTime = startTime.add(1, 'hour');
            $scope.currentLesson.DayOfWeek = day;
            $scope.currentLesson.dateRange.startDate = moment().day(day);
            $scope.currentLesson.StartTime = startTime;
            $scope.currentLesson.EndTime = endTime;
            $scope.mode = 'vote';
            $scope.getCurrentLessonString('Голосование за занятие. ');
        };
        $scope.confirm = function (mode) {
            var mode = mode || $scope.mode;
            var method = 'create';
            var params = {};
            if (mode === 'add' || mode === 'edit' || mode === 'voteForLesson') {
                var startTime = $scope.currentLesson.StartTime;
                var endTime = $scope.currentLesson.EndTime;
                startTime = {hours: startTime.hours(), minutes: startTime.minutes()};
                endTime = {hours: endTime.hours(), minutes: endTime.minutes()};
                var startDate = $scope.currentLesson.dateRange.startDate;
                var endDate = $scope.currentLesson.dateRange.endDate;
                params = {
                    'Type': $scope.currentLesson.Type,
                    'StartTime': startTime,
                    'EndTime': endTime,
                    'Trainer': $scope.currentLesson.Trainer,
                    'PlacesCount': $scope.currentLesson.PlacesCount || 1,
                    'StartDate': startDate?startDate.unix():null,
                    'EndDate': endDate?endDate.unix():null,
                    'Active': $scope.currentLesson.Active || true,
                    'DayOfWeek': startDate.day()
                };
            }
            if (mode === 'edit') {
                method = 'update';
                params.ID = $scope.currentLesson.id;
            } else if (mode === 'bindClientToLesson') {
                method = 'bindClient';
                params = {
                    LessonID: $scope.currentLesson.id,
                    ClientID: $scope.currentLesson.Client
                };
            } else if (mode === 'unbindClient') {
                method = 'unbindClient';
                params = {
                    LessonID: $scope.currentLesson.id,
                    ClientID: $scope.currentLesson.Client
                };
            } else if (mode === 'voteForLesson') {
                method = 'vote';
                angular.extend(params, {
                    'ClientName': $scope.currentClient.Name,
                    'ClientPhone': $scope.currentClient.Phone,
                    'ClientComment': $scope.currentClient.Comment
                });
            }
            Service.dsCall($scope.objectName, method, params)
                .then(function (res) {
                    if (mode === 'unbindClient') {
                        $scope.getLessonClientList();
                    } else {
                        $scope.cancel();
                        $scope.getList();
                    }
                });
        };
        $scope.cancel = function () {
            $scope.mode = $scope.defaultMode;
            $scope.currentLesson = $scope.lessonDefaultState;
        };
        $scope.getList = function () {
            var startDate = $scope.currentWeekDay.startOf('WEEK').unix();
            var endDate = $scope.currentWeekDay.endOf('WEEK').unix();
            var params = {startDate: startDate, endDate: endDate};

            Service.dsCall($scope.objectName, 'get_list', params)
                .then(function (res) {
                    var lessonList = res.data.LessonList;
                    if (lessonList) {
                        $scope.items = lessonList;
                        $scope.renderShedule(lessonList);
                    } else {
                        Service.showError(res.data);
                    }
                });
        };
        $scope.add = function () {
            $scope.mode = 'add';
            $('.selectpicker').selectpicker();
            $scope.getCurrentLessonString('Новое занятие');
        };
        $scope.edit = function (item) {
            $scope.mode = 'edit';
            $scope.currentLesson = item;
        };
        $scope.delete = function (lessonId) {
            var params = {ID: lessonId};

            Service.dsCall($scope.objectName, 'delete', params)
                .then(function (res) {
                    $scope.cancel();
                    $scope.getList();
                });
        };
        $scope.renderShedule = function (lessonList) {
            $scope.weekShedule = {};
            if (lessonList && lessonList.length) {
                lessonList.forEach(function (item) {
                    $scope.weekShedule[item.DayOfWeek + '_' + item.StartTime] = item;
                });
            }
            $scope.mode = $scope.defaultMode;
        };
        $scope.getLessonClientList = function(lesson){
            if (lesson) {
                $scope.currentLesson = lesson;
            }
            $scope.mode = 'clientList';
            Service.getClientList($scope.currentLesson.id).then(function (result) {
                $scope.currentLesson.clientList = result.data.ClientList;
            });
        };
        $scope.getCurrentLessonString = function(prefix){
            var day = moment().day($scope.currentLesson.DayOfWeek).format('dddd');
            $scope.currentLessonString = prefix + day + ', ' + $scope.currentLesson.StartTime;
        };

        getCurrentWeek();
        $scope.getList();
        Service.getTrainerList().then(function (result) {
            $scope.trainerList = result.data.TrainerList;
        });
        Service.getClientList().then(function (result) {
            $scope.clientList = result.data.ClientList;
        });
    }]);
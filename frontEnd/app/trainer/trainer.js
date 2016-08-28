'use strict';

angular.module('trainingShedule.trainer', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/trainer', {
            templateUrl: 'trainer/trainer.html',
            controller: 'TrainerCtrl'
        });
    }])

    .controller('TrainerCtrl', ['$scope', 'Service', function ($scope, Service) {
        $scope.objectName = 'trainer';
        $scope.trainer = {};
        $scope.mode = 'list';

        $scope.confirm = function() {
            debugger;
            var params = {
                'Name': $scope.trainer.Name,
                'Foto': $scope.trainer.Foto,
                'Info': $scope.trainer.Info
            };
            var method = 'create';
            if ($scope.mode === 'edit') {
                method = 'update';
                params.ID = $scope.trainer.ID;
            }

            Service.dsCall($scope.objectName, method, params)
                .then(function (res) {
                    $scope.cancel();
                    $scope.getList();
                });
        };
        $scope.cancel = function() {
            $scope.mode = 'list';
            $scope.trainer = {};
        };
        $scope.getList = function() {
            var params = {};

            Service.dsCall($scope.objectName, 'get_list', params)
                .then(function (res) {
                    if (res.data.TrainerList) {
                        $scope.items = res.data.TrainerList;
                    } else {
                        Service.showError(res.data);
                    }
                });
        };
        $scope.add = function() {
            $scope.mode = 'add';
        };
        $scope.edit = function(item) {
            $scope.mode = 'edit';
            $scope.trainer = item;
        };
        $scope.delete = function(trainerId) {
            debugger;
            var params = {ID: trainerId};

            Service.dsCall($scope.objectName, 'delete', params)
                .then(function (res) {
                    debugger;
                    $scope.cancel();
                    $scope.getList();
                });
        };


        $scope.getList();
    }]);
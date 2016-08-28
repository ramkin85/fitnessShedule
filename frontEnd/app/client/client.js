'use strict';

angular.module('trainingShedule.client', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/client', {
            templateUrl: 'client/client.html',
            controller: 'ClientCtrl'
        });
    }])

    .controller('ClientCtrl', ['$scope', 'Service', function ($scope, Service) {

        $scope.objectName = 'client';
        $scope.client = {};
        $scope.mode = 'list';

        $scope.confirm = function() {
            debugger;
            var params = {
                'Name': $scope.client.Name,
                'Phone': $scope.client.Phone
            };
            var method = 'create';
            if ($scope.mode === 'edit') {
                method = 'update';
                params.id = $scope.client.id;
            }

            Service.dsCall($scope.objectName, method, params)
                .then(function (res) {
                    $scope.cancel();
                    $scope.getList();
                });
        };
        $scope.cancel = function() {
            $scope.mode = 'list';
            $scope.client = {};
        };
        $scope.getList = function() {
            var params = {};

            Service.dsCall($scope.objectName, 'get_list', params)
                .then(function (res) {
                    if (res.data.ClientList) {
                        $scope.items = res.data.ClientList;
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
            $scope.client = item;
        };
        $scope.delete = function(clientId) {
            var params = {id: clientId};

            Service.dsCall($scope.objectName, 'delete', params)
                .then(function (res) {
                    debugger;
                    $scope.cancel();
                    $scope.getList();
                });
        };


        $scope.getList();

    }]);
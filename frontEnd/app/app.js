'use strict';

// Declare app level module which depends on views, and components
var TS = angular.module('trainingShedule', [
    'ngRoute',
    'trainingShedule.shedule',
    'trainingShedule.trainer',
    'trainingShedule.client',
    'trainingShedule.version',
    'daterangepicker',
    'ui.bootstrap'
]);

TS.config(
    function ($httpProvider) {
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
);

/*
TS.config(['$routeProvider', function ($httpProvider, $routeProvider) {
 //$routeProvider.otherwise({redirectTo: '/shedule'});
 $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
 $httpProvider.defaults.xsrfCookieName = 'csrftoken';
 $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
 }]);
*/
TS.controller('tsMainCtrl', function () {

});

TS.service('Service', ['$http', function ($http) {
    var service = {};
    service.dsCall = function (objectName, method, attribs) {
        var url = 'api/' + objectName.toLowerCase();
        attribs.method = method;
        return $http.post(url, attribs, attribs);
        //return $http.get('api', data, params);
        //return $http({'method':'POST', 'url':'api', 'params':params, 'data':params});
    };
    service.showError = function(message) {
        alert(message);
    };
    service.getTrainerList = function(callBack) {
        var params = {};

        return this.dsCall('trainer', 'get_list', params);
    };
    service.getClientList = function(callBack) {
        var params = {};

        return this.dsCall('client', 'get_list', params);
    };

    return service;
}]);
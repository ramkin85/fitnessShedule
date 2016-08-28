'use strict';

angular.module('trainingShedule.version', [
  'trainingShedule.version.interpolate-filter',
  'trainingShedule.version.version-directive'
])

.value('version', '0.1');

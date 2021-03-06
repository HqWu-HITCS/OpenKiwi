"""A generic implementation of a basic tester."""

#  OpenKiwi: Open-Source Machine Translation Quality Estimation
#  Copyright (C) 2019 Unbabel <openkiwi@unbabel.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from kiwi import constants as const


class LinearTester(object):
    def __init__(self, classifier):
        self.classifier = classifier

    def run(self, dataset, **kwargs):
        instances = self.classifier.create_instances(dataset)
        predictions = self.classifier.test(instances)
        self.classifier.evaluate(instances, predictions)
        return {const.TARGET_TAGS: predictions}

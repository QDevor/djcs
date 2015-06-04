#
#            Copyright (C) 2015 QDevor
#
#  Licensed under the GNU General Public License, Version 3.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#            http://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

from sqlalchemy import create_engine
from pandas.io.pytables import HDFStore
import tushare as ts

import ./misc as _

def xls(code='000001'):
    df = ts.get_today_ticks(code)
    save_dir = _.getDataPath() + '/'
    df.to_excel(save_dir + code + '.xlsx')

if __name__ == '__main__':
    xls()
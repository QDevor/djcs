#*- coding: utf-8 -*- 
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

import misc as djcs_misc

def xls(code='000878'):
    df = ts.get_hist_data(code)
    #Ö±½Ó±£´æ
    save_dir = djcs_misc.getDataPath() + '/'
    df.to_excel(save_dir + code + '.xlsx')
    #df.to_excel(save_dir + code + '.xlsx', startrow=2,startcol=5)

def db(code='000878'):
    df = ts.get_tick_data(code,date='2015-04-01')
    engine = create_engine('mysql://root:123456@127.0.0.1/mystock?charset=utf8')
#		db = MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db="mystock",charset="utf8")
#		df.to_sql('TICK_DATA',con=db,flavor='mysql')
#		db.close()
    df.to_sql('tick_data',engine,if_exists='append')
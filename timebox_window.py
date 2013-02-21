# timebox_window.py is an anki2 addon to provide a window with info on timebox stats that doesn't go away until you tell it to
# Copyright 2012 Cayenne Boyer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from anki.hooks import wrap
from anki.collection import _Collection
from aqt.utils import showInfo
from aqt import mw

# Note 1: it seems I should use mw.col instead of the private _Collection, but that seems to be a NoneType when the addon is loaded and so doesn't work

# Note 2: usage of timeboxReached() is seen in reviewer.py

def myTimeboxReached(self, _old):
    ret = _old(self)
    if ret:
        # showInfo(("%(cards)d cards studied in %(mins)s minutes.") % dict(cards=ret[1], mins=ret[0]/60))
        mw.moveToState("overview")
    return ret

_Collection.timeboxReached = wrap(_Collection.timeboxReached, myTimeboxReached, "around")

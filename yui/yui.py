
from ycp import import_module
import_module('Sequencer')
import_module('Wizard')
import_module('UI')
from ycp import Sequencer, Wizard, UI, Symbol, Code

class UISequencer:
    def __init__(self, *cli_args):
        UISequencer.cli_args = cli_args
        UISequencer.itr = 0

    @staticmethod
    def runner():
        UISequencer.funcs[UISequencer.itr](*(UISequencer.cli_args))
        UISequencer.itr += 1

    def run(self, funcs):
        UISequencer.funcs = funcs
        aliases = { 'run%d' % i : Code(UISequencer.runner) for i in range(0, len(UISequencer.funcs)) }

        sequence = { 'run%d' % i : { Symbol('abort') : Symbol('abort'), Symbol('next') : 'run%d' % (i+1) if (i+1) < len(UISequencer.funcs) else Symbol('abort') } for i in range(0, len(UISequencer.funcs)) }
        sequence['ws_start'] = 'run0'

        Wizard.CreateDialog()

        ret = Sequencer.Run(aliases, sequence)

        UI.CloseDialog()
        return ret


import gettext
from gettext import textdomain

textdomain('aduc')

import ycp
ycp.import_module('UI')
from ycp import *
ycp.widget_names()
import Wizard

import sys
import traceback

class DialogTop:
    def UserInput(self):
        while True:
            yield UI.UserInput()

    def QueryWidget(self, _id, symbol):
        return UI.QueryWidget(Term('id', _id), Symbol(symbol))

    def ReplaceWidget(self, _id, contents):
        UI.ReplaceWidget(Term('id', _id), contents)

    def SetFocus(self, _id):
        UI.SetFocus(Term('id', _id))

    def HasSpecialWidget(self, symbol):
        return UI.HasSpecialWidget(Symbol(symbol))

class WizardDialog(DialogTop):
    def __init__(self, title, contents, help_txt, back_txt, next_txt):
        Wizard.SetContentsButtons(gettext.gettext(title), contents, help_txt, back_txt, next_txt)

    def DisableBackButton(self):
        Wizard.DisableBackButton()

    def DisableNextButton(self):
        Wizard.DisableNextButton()

    def DisableAbortButton(self):
        Wizard.DisableAbortButton()

    def EnableAbortButton(self):
        Wizard.EnableAbortButton()

    def EnableNextButton(self):
        Wizard.EnableNextButton()

    def EnableBackButton(self):
        Wizard.EnableBackButton()

class Dialog(DialogTop):
    def __init__(self, contents):
        UI.OpenDialog(contents)

    def CloseDialog(self):
        UI.CloseDialog()

def BarGraph(values, labels, _id=None, opts=[]):
    """Horizontal bar graph (optional widget)

    Synopsis
    BarGraph ( list values, list labels );

    Parameters
    list values

    Optional Arguments
    list labels
    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(values)
        result.append(labels)
        result = tuple(result)

        return BarGraph(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def BusyIndicator(label, timeout=None, _id=None, opts=[]):
    """Graphical busy indicator

    Synopsis
    BusyIndicator ( string label, integer timeout );

    Parameters
    string label  the label describing the bar

    Optional Arguments
    integer timeout  the timeout in milliseconds until busy indicator changes to stalled state, 1000ms by default

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        if timeout:
            result.append(timeout)
        result = tuple(result)

        return BusyIndicator(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ButtonBox(buttons, _id=None, opts=[]):
    """Layout for push buttons that takes button order into account

    Synopsis
    ButtonBox ( term button1, term button2 );

    Parameters
    term buttons  list of PushButton items

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.extend(buttons)
        result = tuple(result)

        return ButtonBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def CheckBox(_id=None, opts=[]):
    """

    Synopsis
    CheckBox (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return CheckBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def CheckBoxFrame(_id=None, opts=[]):
    """

    Synopsis
    CheckBoxFrame (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return CheckBoxFrame(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ComboBox(_id=None, opts=[]):
    """

    Synopsis
    ComboBox (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return ComboBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DateField(_id=None, opts=[]):
    """

    Synopsis
    DateField (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return DateField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DownloadProgress(_id=None, opts=[]):
    """

    Synopsis
    DownloadProgress (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return DownloadProgress(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DumbTab(tabs, contents, _id=None, opts=[]):
    """Simplistic tab widget that behaves like push buttons

    Synopsis
    DumbTab ( list tabs , term contents );

    Parameters
    list tabs  page headers
    term contents  page contents - usually a ReplacePoint
    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if len(opts) > 0:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return DumbTab(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Empty():
    """

    Synopsis
    Empty (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        return Term('Empty')
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Frame(_id=None, opts=[]):
    """

    Synopsis
    Frame (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Frame(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Graph(_id=None, opts=[]):
    """

    Synopsis
    Graph (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Graph(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HBox(children=[], _id=None, opts=[]):
    """Generic layout: Arrange widgets horizontally

    Synopsis
    HBox ( children... );

    Options
    debugLayout  verbose logging

    Optional Arguments
    list children  children widgets

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.extend(children)
        result = tuple(result)

        return HBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VBox(children=[], _id=None, opts=[]):
    """Generic layout: Arrange widgets vertically

    Synopsis
    VBox ( children... );

    Options
    debugLayout  verbose logging

    Optional Arguments
    list children  children widgets

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.extend(children)
        result = tuple(result)

        return VBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HSpacing(_id=None, opts=[]):
    """

    Synopsis
    HSpacing (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return HSpacing(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HSquash(_id=None, opts=[]):
    """

    Synopsis
    HSquash (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return HSquash(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HWeight(weight, child):
    """

    Synopsis
    HWeight ( integer weight, term child );

    Parameters
    integer weight  the new weight of the child widget
    term child  the child widget

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        result.append(weight)
        result.append(child)
        result = tuple(result)

        return HWeight(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Image(_id=None, opts=[]):
    """

    Synopsis
    Image (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Image(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def InputField(_id=None, opts=[]):
    """

    Synopsis
    InputField (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return InputField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def IntField(_id=None, opts=[]):
    """

    Synopsis
    IntField (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return IntField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Label(_id=None, opts=[]):
    """

    Synopsis
    Label (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Label(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Left(_id=None, opts=[]):
    """

    Synopsis
    Left (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Left(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def LogView(_id=None, opts=[]):
    """

    Synopsis
    LogView (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return LogView(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MarginBox(_id=None, opts=[]):
    """

    Synopsis
    MarginBox (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MarginBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MenuButton(_id=None, opts=[]):
    """

    Synopsis
    MenuButton (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MenuButton(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MinWidth(size, child):
    """Layout minimum size

    Synopsis
    MinWidth ( float|integer size, term child );

    Parameters
    float|integer size  minimum width
    term child  The contained child widget

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        result.append(size)
        result.append(child)
        result = tuple(result)

        return MinWidth(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MinHeight(size, child):
    """Layout minimum size

    Synopsis
    MinHeight ( float|integer size, term child );

    Parameters
    float|integer size  minimum heigh
    term child  The contained child widget

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        result.append(size)
        result.append(child)
        result = tuple(result)

        return MinHeight(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MinSize(width, height, child):
    """Layout minimum size

    Synopsis
    MinSize ( float|integer size, float|integer size, term child );

    Parameters
    float|integer size  minimum width
    float|integer size  minimum height
    term child  The contained child widget

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        result.append(width)
        result.append(height)
        result.append(child)
        result = tuple(result)

        return MinSize(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MultiLineEdit(_id=None, opts=[]):
    """

    Synopsis
    MultiLineEdit (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MultiLineEdit(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MultiSelectionBox(_id=None, opts=[]):
    """

    Synopsis
    MultiSelectionBox (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MultiSelectionBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PackageSelector(_id=None, opts=[]):
    """

    Synopsis
    PackageSelector (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PackageSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PartitionSplitter(_id=None, opts=[]):
    """

    Synopsis
    PartitionSplitter (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PartitionSplitter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PatternSelector(_id=None, opts=[]):
    """

    Synopsis
    PatternSelector (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PatternSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ProgressBar(_id=None, opts=[]):
    """

    Synopsis
    ProgressBar (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return ProgressBar(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PushButton(label, _id=None, opts=[]):
    """Perform action on click

    Synopsis
    PushButton ( string label );

    Parameters
    string label

    Options
    default  makes this button the dialogs default button
    helpButton  automatically shows topmost `HelpText
    okButton  assign the [OK] role to this button (see ButtonBox)
    cancelButton  assign the [Cancel] role to this button (see ButtonBox)
    applyButton  assign the [Apply] role to this button (see ButtonBox)
    customButton  override any other button role assigned to this button

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result = tuple(result)

        return PushButton(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RadioButton(_id=None, opts=[]):
    """

    Synopsis
    RadioButton (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return RadioButton(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RadioButtonGroup(_id=None, opts=[]):
    """

    Synopsis
    RadioButtonGroup (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return RadioButtonGroup(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ReplacePoint(child, _id=None, opts=[]):
    """Pseudo widget to replace parts of a dialog

    Synopsis
    ReplacePoint ( term child );

    Parameters
    term child  the child widget
    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if len(opts) > 0:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        result = tuple(result)

        return ReplacePoint(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RichText(_id=None, opts=[]):
    """

    Synopsis
    RichText (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return RichText(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def SelectionBox(_id=None, opts=[]):
    """

    Synopsis
    SelectionBox (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return SelectionBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def SimplePatchSelector(_id=None, opts=[]):
    """

    Synopsis
    SimplePatchSelector (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return SimplePatchSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Slider(_id=None, opts=[]):
    """

    Synopsis
    Slider (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Slider(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Table(header, items=[], _id=None, opts=[]):
    """Multicolumn table widget

    Synopsis
    Table ( term header, list items );

    Parameters
    term header  the headers of the columns

    Optional Arguments
    list items  the items contained in the selection box

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        header = tuple(header)
        result.append(Term('header', *header))
        contents = []
        for item in items:
            contents.append(Term('item', *item))
        result.append(contents)
        result = tuple(result)

        return Table(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def TimeField(_id=None, opts=[]):
    """

    Synopsis
    TimeField (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return TimeField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def TimezoneSelector(_id=None, opts=[]):
    """

    Synopsis
    TimezoneSelector (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return TimezoneSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Node(label, expanded=False, children=[]):
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        result.append(label)
        result.append(expanded)
        result.append(children)
        result = tuple(result)

        return Term('item', *result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Tree(label, items, _id=None, opts=[]):
    """Scrollable tree selection

    Synopsis
    Tree ( string label );

    Parameters
    string label

    Options
    immediate  make `notify trigger immediately when the selected item changes

    Optional Arguments
    itemList items  the items contained in the tree

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result.append(items)
        result = tuple(result)

        return Tree(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VMultiProgressMeter(_id=None, opts=[]):
    """

    Synopsis
    VMultiProgressMeter (  );

    Parameters

    """
    from ycp import *
    ycp.widget_names()

    try:
        result = []
        if _id is not None:
            result.append(Term('id', _id))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return VMultiProgressMeter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)



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
        ret = UISequencer.funcs[UISequencer.itr](*(UISequencer.cli_args))
        UISequencer.itr += 1
        if type(ret) is tuple:
            data, ret = ret
            UISequencer.cli_args = (data,) + UISequencer.cli_args
        return ret

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
    @staticmethod
    def UserInput():
        while True:
            yield UI.UserInput()

    @staticmethod
    def QueryWidget(ID, symbol):
        return UI.QueryWidget(Term('id', ID), Symbol(symbol))

    @staticmethod
    def ReplaceWidget(ID, contents):
        UI.ReplaceWidget(Term('id', ID), contents)

    @staticmethod
    def SetFocus(ID):
        UI.SetFocus(Term('id', ID))

    @staticmethod
    def HasSpecialWidget(symbol):
        return UI.HasSpecialWidget(Symbol(symbol))

class WizardDialog(DialogTop):
    @staticmethod
    def SetContentsButtons(title, contents, help_txt, back_txt, next_txt):
        Wizard.SetContentsButtons(gettext.gettext(title), contents, help_txt, back_txt, next_txt)

    @staticmethod
    def DisableBackButton():
        Wizard.DisableBackButton()

    @staticmethod
    def DisableNextButton():
        Wizard.DisableNextButton()

    @staticmethod
    def DisableAbortButton():
        Wizard.DisableAbortButton()

    @staticmethod
    def EnableAbortButton():
        Wizard.EnableAbortButton()

    @staticmethod
    def EnableNextButton():
        Wizard.EnableNextButton()

    @staticmethod
    def EnableBackButton():
        Wizard.EnableBackButton()

class Dialog(DialogTop):
    @staticmethod
    def OpenDialog(contents):
        UI.OpenDialog(contents)

    @staticmethod
    def CloseDialog():
        UI.CloseDialog()

def BarGraph(values, labels, ID=None, opts=[]):
    """Horizontal bar graph (optional widget)

    Synopsis
    BarGraph ( list values, list labels );

    Parameters
    list values

    Optional Arguments
    list labels
    """
    from ycp import BarGraph, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
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

def BusyIndicator(label, timeout=None, ID=None, opts=[]):
    """Graphical busy indicator

    Synopsis
    BusyIndicator ( string label, integer timeout );

    Parameters
    string label  the label describing the bar

    Optional Arguments
    integer timeout  the timeout in milliseconds until busy indicator changes to stalled state, 1000ms by default

    """
    from ycp import BusyIndicator, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
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

def ButtonBox(buttons, ID=None, opts=[]):
    """Layout for push buttons that takes button order into account

    Synopsis
    ButtonBox ( term button1, term button2 );

    Parameters
    term buttons  list of PushButton items

    """
    from ycp import ButtonBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.extend(buttons)
        result = tuple(result)

        return ButtonBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def CheckBox(ID=None, opts=[]):
    """

    Synopsis
    CheckBox (  );

    Parameters

    """
    from ycp import CheckBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return CheckBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def CheckBoxFrame(ID=None, opts=[]):
    """

    Synopsis
    CheckBoxFrame (  );

    Parameters

    """
    from ycp import CheckBoxFrame, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return CheckBoxFrame(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ComboBox(label, items=[], ID=None, opts=[]):
    """drop-down list selection (optionally editable)

    Synopsis
    ComboBox ( string label, list items );

    Parameters
    string label

    Options
    editable  the user can enter any value.

    Optional Arguments
    list items  the items contained in the combo box

    """
    from ycp import ComboBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        options = []
        for item in items:
            if type(item) is tuple:
                options.append(Term('item', *item))
            else:
                options.append(item)
        result.append(options)
        result = tuple(result)

        return ComboBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DateField(ID=None, opts=[]):
    """

    Synopsis
    DateField (  );

    Parameters

    """
    from ycp import DateField, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return DateField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DownloadProgress(ID=None, opts=[]):
    """

    Synopsis
    DownloadProgress (  );

    Parameters

    """
    from ycp import DownloadProgress, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return DownloadProgress(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def DumbTab(tabs, contents, ID=None, opts=[]):
    """Simplistic tab widget that behaves like push buttons

    Synopsis
    DumbTab ( list tabs , term contents );

    Parameters
    list tabs  page headers
    term contents  page contents - usually a ReplacePoint
    """
    from ycp import DumbTab, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if len(opts) > 0:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(tabs)
        result.append(contents)
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
    from ycp import Term
    ycp.widget_names()

    try:
        return Term('Empty')
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Frame(label, child, ID=None, opts=[]):
    """Frame with label

    Synopsis
    Frame ( string label, term child );

    Parameters
    string label  title to be displayed on the top left edge
    term child  the contained child widget

    """
    from ycp import Frame, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result.append(child)
        result = tuple(result)

        return Frame(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Graph(ID=None, opts=[]):
    """

    Synopsis
    Graph (  );

    Parameters

    """
    from ycp import Graph, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Graph(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HBox(*children):
    """Generic layout: Arrange widgets horizontally

    Synopsis
    HBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    from ycp import HBox
    ycp.widget_names()

    try:
        return HBox(*children)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VBox(*children):
    """Generic layout: Arrange widgets vertically

    Synopsis
    VBox ( children... );

    Optional Arguments
    list children  children widgets

    """
    from ycp import VBox
    ycp.widget_names()

    try:
        return VBox(*children)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HSpacing(size=None):
    """Fixed size empty space for layout

    Synopsis
    HSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    from ycp import HSpacing, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if size is not None:
            result.append(size)
        result = tuple(result)

        return HSpacing(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VSpacing(size=None):
    """Fixed size empty space for layout

    Synopsis
    VSpacing ( integer|float size );

    Optional Arguments
    integer|float size

    """
    from ycp import VSpacing, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if size is not None:
            result.append(size)
        result = tuple(result)

        return VSpacing(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HStretch(size=None):
    """Fixed size empty space for layout

    Synopsis
    HStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    from ycp import HStretch, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if size is not None:
            result.append(size)
        result = tuple(result)

        return HStretch(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VStretch(size=None):
    """Fixed size empty space for layout

    Synopsis
    VStretch ( integer|float size );

    Optional Arguments
    integer|float size

    """
    from ycp import VStretch, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if size is not None:
            result.append(size)
        result = tuple(result)

        return VStretch(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HSquash(ID=None, opts=[]):
    """

    Synopsis
    HSquash (  );

    Parameters

    """
    from ycp import HSquash, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
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
    from ycp import HWeight
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

def Image(ID=None, opts=[]):
    """

    Synopsis
    Image (  );

    Parameters

    """
    from ycp import Image, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Image(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def InputField(label, defaulttext=None, ID=None, opts=[]):
    """Input field

    Synopsis
    InputField ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    from ycp import InputField, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        if defaulttext is not None:
            result.append(defaulttext)
        result = tuple(result)

        return InputField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def TextEntry(label, defaulttext=None, ID=None, opts=[]):
    """Input field

    Synopsis
    TextEntry ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    from ycp import TextEntry, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        if defaulttext is not None:
            result.append(defaulttext)
        result = tuple(result)

        return TextEntry(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Password(label, defaulttext=None, ID=None, opts=[]):
    """Input field

    Synopsis
    Password ( string label, string defaulttext );

    Parameters
    string label  the label describing the meaning of the entry

    Options
    shrinkable  make the input field very small

    Optional Arguments
    string defaulttext  The text contained in the text entry

    """
    from ycp import Password, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        if defaulttext is not None:
            result.append(defaulttext)
        result = tuple(result)

        return Password(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def IntField(ID=None, opts=[]):
    """

    Synopsis
    IntField (  );

    Parameters

    """
    from ycp import IntField, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return IntField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Label(label, ID=None, opts=[]):
    """Simple static text

    Synopsis
    Label ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    from ycp import Label, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result = tuple(result)

        return Label(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Heading(label, ID=None, opts=[]):
    """Simple static text

    Synopsis
    Heading ( string label );

    Parameters
    string label

    Options
    outputField  make the label look like an input field in read-only mode
    boldFont  use a bold font

    """
    from ycp import Heading, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result = tuple(result)

        return Heading(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Left(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Left ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import Left, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return Left(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Right(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Right ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import Right, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return Right(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Top(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Top ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import Top, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return Top(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Bottom(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    Bottom ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import Bottom, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return Bottom(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    HCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import HCenter, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return HCenter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def VCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    VCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import VCenter, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return VCenter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def HVCenter(child, pixmap=None, ID=None, opts=[]):
    """Layout alignment

    Synopsis
    HVCenter ( term child, string pixmap );

    Parameters
    term child  The contained child widget

    Optional Arguments
    background pixmap

    """
    from ycp import HVCenter, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        if pixmap is not None:
            result.append(Term('BackgroundPixmap', pixmap))
        result = tuple(result)

        return HVCenter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def LogView(ID=None, opts=[]):
    """

    Synopsis
    LogView (  );

    Parameters

    """
    from ycp import LogView, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return LogView(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MarginBox(ID=None, opts=[]):
    """

    Synopsis
    MarginBox (  );

    Parameters

    """
    from ycp import MarginBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MarginBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MenuButton(ID=None, opts=[]):
    """

    Synopsis
    MenuButton (  );

    Parameters

    """
    from ycp import MenuButton, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
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
    from ycp import MinWidth
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
    from ycp import MinHeight
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
    from ycp import MinSize
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

def MultiLineEdit(ID=None, opts=[]):
    """

    Synopsis
    MultiLineEdit (  );

    Parameters

    """
    from ycp import MultiLineEdit, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MultiLineEdit(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def MultiSelectionBox(ID=None, opts=[]):
    """

    Synopsis
    MultiSelectionBox (  );

    Parameters

    """
    from ycp import MultiSelectionBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return MultiSelectionBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PackageSelector(ID=None, opts=[]):
    """

    Synopsis
    PackageSelector (  );

    Parameters

    """
    from ycp import PackageSelector, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PackageSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PartitionSplitter(ID=None, opts=[]):
    """

    Synopsis
    PartitionSplitter (  );

    Parameters

    """
    from ycp import PartitionSplitter, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PartitionSplitter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PatternSelector(ID=None, opts=[]):
    """

    Synopsis
    PatternSelector (  );

    Parameters

    """
    from ycp import PatternSelector, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return PatternSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ProgressBar(ID=None, opts=[]):
    """

    Synopsis
    ProgressBar (  );

    Parameters

    """
    from ycp import ProgressBar, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return ProgressBar(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def PushButton(label, ID=None, opts=[]):
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
    from ycp import PushButton, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(label)
        result = tuple(result)

        return PushButton(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RadioButton(ID=None, opts=[]):
    """

    Synopsis
    RadioButton (  );

    Parameters

    """
    from ycp import RadioButton, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return RadioButton(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RadioButtonGroup(ID=None, opts=[]):
    """

    Synopsis
    RadioButtonGroup (  );

    Parameters

    """
    from ycp import RadioButtonGroup, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return RadioButtonGroup(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def ReplacePoint(child, ID=None, opts=[]):
    """Pseudo widget to replace parts of a dialog

    Synopsis
    ReplacePoint ( term child );

    Parameters
    term child  the child widget
    """
    from ycp import ReplacePoint, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if len(opts) > 0:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(child)
        result = tuple(result)

        return ReplacePoint(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def RichText(text, ID=None, opts=[]):
    """Static text with HTML-like formatting

    Synopsis
    RichText ( string text );

    Parameters
    string text

    Options
    plainText  don't interpret text as HTML
    autoScrollDown  automatically scroll down for each text change
    shrinkable  make the widget very small

    """
    from ycp import RichText, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result.append(text)
        result = tuple(result)

        return RichText(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def SelectionBox(ID=None, opts=[]):
    """

    Synopsis
    SelectionBox (  );

    Parameters

    """
    from ycp import SelectionBox, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return SelectionBox(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def SimplePatchSelector(ID=None, opts=[]):
    """

    Synopsis
    SimplePatchSelector (  );

    Parameters

    """
    from ycp import SimplePatchSelector, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return SimplePatchSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Slider(ID=None, opts=[]):
    """

    Synopsis
    Slider (  );

    Parameters

    """
    from ycp import Slider, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return Slider(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Table(header, items=[], ID=None, opts=[]):
    """Multicolumn table widget

    Synopsis
    Table ( term header, list items );

    Parameters
    term header  the headers of the columns

    Optional Arguments
    list items  the items contained in the selection box

    """
    from ycp import Table, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        header = tuple(header)
        result.append(Term('header', *header))
        contents = []
        for item in items:
            if type(item) is list:
                contents.append(Term('item', Term('id', item[0]), *(item[1])))
            else:
                contents.append(Term('item', *item))
        result.append(contents)
        result = tuple(result)

        return Table(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def TimeField(ID=None, opts=[]):
    """

    Synopsis
    TimeField (  );

    Parameters

    """
    from ycp import TimeField, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return TimeField(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def TimezoneSelector(ID=None, opts=[]):
    """

    Synopsis
    TimezoneSelector (  );

    Parameters

    """
    from ycp import TimezoneSelector, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return TimezoneSelector(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Node(label, expanded=False, children=[], ID=None):
    from ycp import Term
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        result.append(label)
        result.append(expanded)
        result.append(children)
        result = tuple(result)

        return Term('item', *result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

def Tree(label, items, ID=None, opts=[]):
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
    from ycp import Tree, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
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

def VMultiProgressMeter(ID=None, opts=[]):
    """

    Synopsis
    VMultiProgressMeter (  );

    Parameters

    """
    from ycp import VMultiProgressMeter, Term, Symbol
    ycp.widget_names()

    try:
        result = []
        if ID is not None:
            result.append(Term('id', ID))
        if opts is not None:
            for opt in opts:
                result.append(Term('opt', Symbol(opt)))
        result = tuple(result)

        return VMultiProgressMeter(*result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)


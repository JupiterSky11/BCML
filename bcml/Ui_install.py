# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\macad\Documents\Git\BCML-2\.vscode\install.ui',
# licensing of 'c:\Users\macad\Documents\Git\BCML-2\.vscode\install.ui' applies.
#
# Created: Sun Jul 28 13:21:19 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_InstallDialog(object):
    def setupUi(self, InstallDialog):
        InstallDialog.setObjectName("InstallDialog")
        InstallDialog.setWindowModality(QtCore.Qt.WindowModal)
        InstallDialog.resize(400, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InstallDialog.sizePolicy().hasHeightForWidth())
        InstallDialog.setSizePolicy(sizePolicy)
        InstallDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(InstallDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(InstallDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtFile = QtWidgets.QLineEdit(InstallDialog)
        self.txtFile.setObjectName("txtFile")
        self.horizontalLayout.addWidget(self.txtFile)
        self.btnBrowse = QtWidgets.QPushButton(InstallDialog)
        self.btnBrowse.setStyleSheet("padding: 3px 8px;")
        self.btnBrowse.setObjectName("btnBrowse")
        self.horizontalLayout.addWidget(self.btnBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(InstallDialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chkRstbLeave = QtWidgets.QCheckBox(self.groupBox)
        self.chkRstbLeave.setObjectName("chkRstbLeave")
        self.verticalLayout_2.addWidget(self.chkRstbLeave)
        self.chkRstbShrink = QtWidgets.QCheckBox(self.groupBox)
        self.chkRstbShrink.setObjectName("chkRstbShrink")
        self.verticalLayout_2.addWidget(self.chkRstbShrink)
        self.chkDisablePack = QtWidgets.QCheckBox(self.groupBox)
        self.chkDisablePack.setObjectName("chkDisablePack")
        self.verticalLayout_2.addWidget(self.chkDisablePack)
        self.chkDisableTexts = QtWidgets.QCheckBox(self.groupBox)
        self.chkDisableTexts.setObjectName("chkDisableTexts")
        self.verticalLayout_2.addWidget(self.chkDisableTexts)
        self.chkDisableActorInfo = QtWidgets.QCheckBox(self.groupBox)
        self.chkDisableActorInfo.setObjectName("chkDisableActorInfo")
        self.verticalLayout_2.addWidget(self.chkDisableActorInfo)
        self.chkDisableGamedata = QtWidgets.QCheckBox(self.groupBox)
        self.chkDisableGamedata.setObjectName("chkDisableGamedata")
        self.verticalLayout_2.addWidget(self.chkDisableGamedata)
        self.chkDisableSavedata = QtWidgets.QCheckBox(self.groupBox)
        self.chkDisableSavedata.setObjectName("chkDisableSavedata")
        self.verticalLayout_2.addWidget(self.chkDisableSavedata)
        self.chkEnableDeepMerge = QtWidgets.QCheckBox(self.groupBox)
        self.chkEnableDeepMerge.setObjectName("chkEnableDeepMerge")
        self.verticalLayout_2.addWidget(self.chkEnableDeepMerge)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(18)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.chkDelayMerge = QtWidgets.QCheckBox(self.groupBox)
        self.chkDelayMerge.setObjectName("chkDelayMerge")
        self.verticalLayout_2.addWidget(self.chkDelayMerge)
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(InstallDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(InstallDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), InstallDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), InstallDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InstallDialog)

    def retranslateUi(self, InstallDialog):
        InstallDialog.setWindowTitle(QtWidgets.QApplication.translate("InstallDialog", "Install Mod", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("InstallDialog", "Select Mod:", None, -1))
        self.btnBrowse.setToolTip(QtWidgets.QApplication.translate("InstallDialog", "Browse for a mod", None, -1))
        self.btnBrowse.setText(QtWidgets.QApplication.translate("InstallDialog", "Browse...", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("InstallDialog", "Advanced Install Options", None, -1))
        self.chkRstbLeave.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t delete RSTB entries for files which can\'t be calculated\n"
"(May cause instability, use with caution)", None, -1))
        self.chkRstbShrink.setText(QtWidgets.QApplication.translate("InstallDialog", "Shrink RSTB values where possible", None, -1))
        self.chkDisablePack.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t attempt to merge packs", None, -1))
        self.chkDisableTexts.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t attempt to merge texts", None, -1))
        self.chkDisableActorInfo.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t attempt to merge actor info", None, -1))
        self.chkDisableGamedata.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t attempt to merge game data", None, -1))
        self.chkDisableSavedata.setText(QtWidgets.QApplication.translate("InstallDialog", "Don\'t attempt to merge save data", None, -1))
        self.chkEnableDeepMerge.setText(QtWidgets.QApplication.translate("InstallDialog", "Deep merge (experimental)", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("InstallDialog", "Deep merge attempts to merge changes made to individual files of certain kinds. This can be a powerful tool to resolve conflicts but can also potentially cause unexpected bugs or issues. ", None, -1))
        self.chkDelayMerge.setText(QtWidgets.QApplication.translate("InstallDialog", "Install but wait to run merge manually", None, -1))

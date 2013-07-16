# -*- coding: UTF-8 -*-
#Plugin to switch only between Talk or Off speech modes
#Author: Alberto Buffolino
#Last update: 13.03.2013

import addonHandler
import globalPluginHandler
import ui
import speech
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_noBeepsSpeechMode(self, gesture):
		curMode=speech.speechMode
		if curMode==speech.speechMode_talk:
			# change order of two next lines of code to having no speech message about off
			# (direct off mode, with only Braille message, if active)
			# Translators: A speech mode which disables speech output.
			ui.message(_("speech mode %s")%_("off"))
			speech.speechMode=speech.speechMode_off
		elif curMode==speech.speechMode_off:
			speech.speechMode=speech.speechMode_talk
			# Translators: The normal speech mode; i.e. NVDA will talk as normal.
			ui.message(_("speech mode %s")%_("talk"))
	# Translators: Message presented in input help mode.
	script_noBeepsSpeechMode.__doc__=_("Toggles between the speech modes of off and talk. When set to off NVDA will not speak anything. If talk then NVDA wil just speak normally.")

	__gestures = {
		"kb:NVDA+s": "noBeepsSpeechMode",
	}
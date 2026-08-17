# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['run_app.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Ship the entire frontend folder inside the bundle
        ('frontend', 'frontend'),
    ],
    hiddenimports=[
        # uvicorn dynamic imports
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
        # SQLAlchemy SQLite dialect
        'sqlalchemy.dialects.sqlite',
        'sqlalchemy.sql.default_comparator',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Krishna Chains',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,      # No terminal window — users interact via the browser
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Krishna Chains',
)

# Mac .app bundle
app = BUNDLE(
    coll,
    name='Krishna Chains.app',
    icon=None,          # swap None for 'icon.icns' when you have an icon
    bundle_identifier='com.krishnachains.billing',
    info_plist={
        'CFBundleDisplayName': 'Krishna Chains',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSPrincipalClass': 'NSApplication',
        'LSMinimumSystemVersion': '10.15.0',
        'NSAppleScriptEnabled': False,
    },
)

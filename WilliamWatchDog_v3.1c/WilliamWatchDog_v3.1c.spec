# -*- mode: python -*-

block_cipher = None


a = Analysis(['WilliamWatchDog_v3.1c.py'],
             pathex=['C:\\Users\\funqiue\\Desktop\\Python Test\\WilliamWatchDog_v3.1c'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='WilliamWatchDog_v3.1c',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

import os
from functools import reduce

package_name = 'piculator-system'
name = 'piculator-system'
desp = 'Piculatorize your raspberry pi zero'
version = input('Please input version:')
package_path = f'{package_name}_{version}'
os.makedirs(f"{package_path}/DEBIAN", exist_ok=True)
dependencies = {
    'piculator-client': '=1.0-1',
    'piculator-localhost': '=1.0-1',
    'piculator-mu-editor': '=1.0.3+dfsg-2',
    'piculator-plym-splash': '=1.0-1',
    'piculator-sagemath': '=9.2-1',
    'piculator-sage-documentation-en': '=1.0-1',
    'piculator-chinese-support': '=1.0-1',
    'piculator-static-gamma': '=1.0-1',
    'piculator-static-icons': '=1.0.1-1',
    'piculator-static-stopwatch': '=1.0-1',
    'piculator-xmodkey': '=1.0-1',
}
depends = reduce(lambda x,y:x+y,\
    map(lambda z: z+ \
        (f' ({dependencies[z]}), ' if dependencies[z] is not None else ', '),\
        dependencies.keys()))[:-2]
control_content = f'''Package: {package_name}
Architecture: all
Name: {name}
Description: {desp}
Version: {version}
Section: base
Depends: {depends}
Author: Piculator Development Team <piculator@protonmail.com>
Maintainer: Piculator Development Team <piculator@protonmail.com>
HomePage: https://github.com/piculator/{package_name}-software
'''
ctl_file = open(f'{package_path}/DEBIAN/control', mode='w+')
ctl_file.write(control_content)
ctl_file.close()
os.system(f'dpkg-deb -b {package_path}')

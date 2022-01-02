# disasm-mips

调用OBJDUMP来完成反汇编的简单脚本。供同学们简单查询汇编使用。

## 环境搭建

可以使用Debian/Ubuntu系统，安装以下软件包：

```bash
apt install gcc-mipsel-linux-gnu
```

使用Windows系统的同学用WSL的Ubuntu也可以。

## 使用方法

1. 交互模式

直接运行：`python3 disasm-mips.py`

```bash
$ python3 disasm-mips.py 
>>> deadbeef
ld      t5,-16657(s5)
>>> 20020005
addi    v0,zero,5
>>> 2003000c
addi    v1,zero,12
>>> 
```

2. coe模式

```bash
python3 disasm-mips.py /home/cyy/step_into_mips/lab_4/coe/mipstest.coe
```

```bash
python3 disasm-mips.py /home/cyy/step_into_mips/lab_4/coe/mipstest.coe

disasm.bin:     file format binary


Disassembly of section .data:

00000000 <.data>:
   0:   05000220        addi    v0,zero,5
   4:   0c000320        addi    v1,zero,12
   8:   f7ff6720        addi    a3,v1,-9
   c:   2520e200        or      a0,a3,v0
  10:   24286400        and     a1,v1,a0
  14:   2028a400        add     a1,a1,a0
  18:   0c00a710        beq     a1,a3,0x4c
  1c:   2a206400        slt     a0,v1,a0
  20:   02008010        beqz    a0,0x2c
  24:   00000000        nop
  28:   00000520        addi    a1,zero,0
  2c:   2a20e200        slt     a0,a3,v0
  30:   20388500        add     a3,a0,a1
  34:   2238e200        sub     a3,a3,v0
  38:   440067ac        sw      a3,68(v1)
  3c:   5000028c        lw      v0,80(zero)
  40:   13000008        j       0x4c
  44:   00000000        nop
  48:   01000220        addi    v0,zero,1
  4c:   540002ac        sw      v0,84(zero)
```
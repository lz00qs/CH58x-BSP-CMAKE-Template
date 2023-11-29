#include "CH58x_common.h"
#define LED_Pin GPIO_Pin_19

int main()
{
    SetSysClock(CLK_SOURCE_PLL_60MHz);
    GPIOB_ModeCfg(LED_Pin, GPIO_ModeOut_PP_5mA);

    while (1)
    {
        GPIOB_SetBits(LED_Pin);
        DelayMs(500);
        GPIOB_ResetBits(LED_Pin);
        DelayMs(500);
    }
}
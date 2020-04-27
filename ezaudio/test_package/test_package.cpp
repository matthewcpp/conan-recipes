#define EZAUDIO_IMPLEMENTATION
#include <ezaudio/ezaudio.h>


int main(int argc, char** argv) {

    ez_audio_params params;
    ez_audio_init_params(&params);
    auto ez_audio = ez_audio_create(&params);
    ez_audio_destroy(ez_audio);

    return 0;
}
